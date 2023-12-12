import pygame as pg
import sys
import os
# личные модули
from libs.sprite import *     # Sprites
from libs.movement import *   # Movement
from configs.config import *
from frames import *
# from libs.decrypt import *    # decrypt config file

key = "PSD1LpXi3H77JX7B5_dcm29sjXcmN5fDa5tgnEP8ySg="

def full_path(path_key: str) -> list[list[str]]:
    "takes paths of sprites from json file by key"
    IMG_DIR = "img"
    return [[os.path.join(IMG_DIR, path) for path in i] for i in frames[path_key]]

# Задаём пути к папкам с изображениями через файл json
bg = os.path.join("img", "backgrounds", "bgpsdraw.png")
MAIN_CHAR = full_path("main_character")
ASTEROID_1 = full_path("asteroid_1")
ASTEROIDS_1 = full_path("asteroid")
ASTEROIDS_2 = full_path("asteroid")
ASTEROIDS_3 = full_path("asteroid")


class Game:
    def __init__(self) -> None:
        pg.init() # инициализация пайгейм на всякий пожарный
        # with open("configs/config.json", "r") as file:
        #     configs = json.load(file)
        #     self.w = configs["width"]
        #     self.h = configs["height"]
        #     self.score = configs["score"]
        self.w = game_config["width"]
        self.h = game_config["height"]
        self.score = game_config["score"]
        self.speed = 8
        self.screen = pg.display.set_mode((self.w, self.h), pg.RESIZABLE)
        pg.display.set_caption("Jersey")
        self.running = True # Работа основного цикла игры
        self.clock = pg.time.Clock() # Экземпляр класса работы тиков
        self.tick = 0 # Тик на данный момент
        self.font =  pg.font.Font(None, 36)
        self.active_infobar = False
        # Загружаем изображение фона
        self.bg = pg.image.load(bg).convert()
        # Создание спрайтов
        self.asteroid_sprite_1 = self.create_sprite(ASTEROID_1, mode=1)
        self.main_char = self.create_sprite(MAIN_CHAR, 0.15, mode=1)
        self.pos = self.w*0.5+self.h*0.5j # позиция основного игрока
        self.tvector = Vector()
        self.fps = [0]*72
        self.click = None
        self.pressed = {}
        self.bg_pos = [0.0, 0.0]
        self.main_char_mask = pg.mask.from_surface(list(self.main_char)[0].image)
        self.asteroid_mask = pg.mask.from_surface(list(self.asteroid_sprite_1)[0].image)
        self.run() # Вызов основного игрового цикла

    def run(self) -> None:
        "Main Game cycle"
        while self.running:
            self.tick += 1 if self.tick < 71 else -71
            self.key = pg.key.get_pressed()
            self.key_pressed()
            self.handle_events()
            self.update()
            self.draw()
            self.fps = self.fps[1:] + [self.clock.get_fps()] # лист фпс за последние 10 кадров


            # print(self.main_char_rect.colliderect(list(self.asteroid_sprite_1)[0].get_srect()))
            if self.main_char_mask.overlap(self.asteroid_mask, (500-self.pos.real, 300-self.pos.imag)) is not None:
                print(True)
            else:
                print(False)


            # print(self.fps)

    def handle_events(self) -> None:
        "Обработчик событий"
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                # Обработка изменения размера окна
                self.w = event.w
                self.h = event.h
                self.screen = pg.display.set_mode((self.w, self.h), pg.RESIZABLE)
            elif event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_F3 and not self.active_infobar:
                    self.active_infobar = True
                elif event.key == pg.K_F3 and self.active_infobar:
                    self.active_infobar = False

    def update(self) -> None:
        "updating sprites"
        "Отрисовка спрайтов"
        for sprite in self.asteroid_sprite_1:
            sprite.update()
            sprite.move(complex(500, 300), "topleft")

        for sprite in self.main_char:
            sprite.update(index=0, rate=2.5)
            sprite.move(self.pos, "center")

    def draw(self) -> None:
        "draws on the screen"
        self.screen.blit(self.bg, self.bg_pos) # Рисуем Фон

        # Рисуем спрайты
        self.asteroid_sprite_1.draw(self.screen)
        self.main_char.draw(self.screen)

        self.infobar()


        pg.display.flip() # updates the screen
        self.clock.tick(72)  # Ограничиваем частоту обновления кадров

    def key_pressed(self) -> None:
        "pressed key"
        self.tvector.z = 0
        if self.key[pg.K_w]: self.tvector.z += (-self.speed*1j)
        if self.key[pg.K_s]: self.tvector.z += (self.speed*1j)
        if self.key[pg.K_a]: self.tvector.z += (-self.speed)
        if self.key[pg.K_d]: self.tvector.z += (self.speed)
        self.tvector.norm_speed()
        self.tvector.inertia()

        if self.bg_pos[0] - self.tvector.z.real <= 0:
            if self.pos.real+self.tvector.z.real <= self.w*(1/3) and self.pos.real > self.w*(1/3):
                self.bg_pos[0] -= self.tvector.z.real
                self.tvector.block([0, 1])
        if self.bg_pos[0] - self.tvector.z.real >= -3840+self.w:
            if self.pos.real+self.tvector.z.real >= self.w*(2/3) and self.pos.real > (-3840+self.w)*(2/3):
                print(self.pos.real, (-3840+self.w)/4*3)
                self.bg_pos[0] -= self.tvector.z.real
                self.tvector.block([0, 1]) # блокируется перемещение по X
        if self.pos.imag+self.tvector.z.imag <= self.h*(1/3) and self.pos.imag > self.h*(1/3):
            self.bg_pos[1] -= self.tvector.z.imag
            self.tvector.block([1, 0]) # блокируется перемещение по Y
        if self.pos.imag+self.tvector.z.imag >= self.h*(2/3):
            self.bg_pos[1] -= self.tvector.z.imag
            self.tvector.block([1, 0])  # блокируется перемещение по Y
        
        
        if self.pos.real + self.tvector.z.real < 0:
            self.tvector.block([0, 1])
        self.pos += self.tvector()

    def infobar(self) -> None:
        if self.active_infobar:
            text = [f"FPS: {round(sum(self.fps)/72)}", 
                    f"Position: X {round(self.pos.real-self.bg_pos[0])}; Y {round(self.pos.imag-self.bg_pos[1])}",
                    f"Moving vector: X {round(self.tvector.z.real)}; Y {round(self.tvector.z.imag)}",
                    ]
            for i in range(len(text)):
                self.screen.blit(self.font.render(text[i], True, "white"), (10, 10+i*36))
        else:
            pass
        

    @staticmethod
    def create_sprite(frames, k: float = 1.0, mode=0) -> pg.sprite.Group:
        "creates a group of sprites from a given list of images"
        if not mode:  # Надо постараться удалить это
            images = [pg.image.load(image).convert_alpha() for image in frames]
            if k!=1.0:
                images = [pg.transform.scale(image, (int(image.get_width() * k), int(image.get_height() * k))) for image in images]
            sprite = Sprite()
            sprite.set_sprite(images)
            return pg.sprite.Group(sprite)
        else:
            images = [[pg.image.load(image) for image in i] for i in frames]
            if k==1.0:
                pass
            else:
                images = [[pg.transform.scale(image, (int(image.get_width() * k), int(image.get_height() * k))) for image in i] for i in images]
            sprite = Sprite()
            sprite.set_sprite(images)
            return pg.sprite.Group(sprite)


if __name__ == "__main__":
    # import cProfile
    # cProfile.run("Game()", sort="cumulative")
    game = Game()
    pg.quit()
    sys.exit()
