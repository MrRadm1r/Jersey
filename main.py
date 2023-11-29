import pygame as pg
import sys
import os
import json
# личные модули
from libs.sprite import Sprite
from libs.complex import *

# Задаём пути к папкам с изображениями через файл json
with open("frames.json", "r") as file:
    frames = json.load(file)
    IMG_DIR = "img"
    bg = os.path.join(IMG_DIR, "backgrounds", "bg.png")
    BIGBG = os.path.join(IMG_DIR, "backgrounds", "BIGBG.png")
    FIRE_IMAGES = [os.path.join(IMG_DIR, i) for i in frames["fire"]]
    ASTEROID_1 = [os.path.join(IMG_DIR, i) for i in frames["asteroid_1"]]
    MAIN_CHAR = [os.path.join(IMG_DIR, i) for i in frames["main_character"]]
    del IMG_DIR

class Game:
    def __init__(self):
        self.w = 1400
        self.h = 800
        self.speed = 8
        self.l = 15
        self.fsc = [0]*self.l
        self.ssc = [0]*self.l
        self.dsc = [[0j]*self.l]*2
        pg.init() # инициализация пайгейм на всякий пожарный
        self.screen = pg.display.set_mode((self.w, self.h), pg.RESIZABLE)
        pg.display.set_caption("Jersey")
        self.running = True # Работа основного цикла игры
        self.clock = pg.time.Clock() # Экземпляр класса работы тиков
        self.tick = 0 # Тик на данный момент

        # Загружаем изображение фона
        self.bg = pg.image.load(bg).convert()
        self.BIGBG = pg.image.load(BIGBG).convert()
        # Создание спрайтов
        self.asteroid_sprite_1 = self.create_sprite(ASTEROID_1)
        self.fire_sprite = self.create_sprite(FIRE_IMAGES, 0.2)
        self.main_char = self.create_sprite(MAIN_CHAR, 0.15)
        self.pos = self.w*0.5+self.h*0.5j # позиция основного игрока
        self.tvector = 0
        self.fps = []
        self.run() # Вызов основного игрового цикла

    def run(self):
        # Основной игровой цикл
        while self.running:
            self.tick += 1 if self.tick < 71 else -71
            self.key = pg.key.get_pressed()
            self.key_pressed()
            self.handle_events()
            self.update()
            self.draw()
            # self.fps.append(self.clock.get_fps())
            # print(sum(self.fps)/len(self.fps))
            # print(self.fps)

    def handle_events(self) -> None:
        "Обработчик событий"
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                # Обработка изменения размера окна
                self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            elif event.type == pg.QUIT:
                self.running = False

    def update(self) -> None:
        "Отрисовка спрайтов"
        for sprite in self.asteroid_sprite_1:
            sprite.update(self.tick)
            sprite.move(complex(0, 400), "topleft")

        for sprite in self.fire_sprite:
            sprite.update(self.tick, rate=2.5)
            sprite.move(self.pos+100j, "center")

        for sprite in self.main_char:
            sprite.char_update(0)
            sprite.move(self.pos, "center")

    def draw(self) -> None:
        "draws on the screen"
        self.screen.blit(self.bg, (0, 0)) # Рисуем Фон

        # Рисуем спрайты
        self.asteroid_sprite_1.draw(self.screen)
        self.fire_sprite.draw(self.screen)
        self.main_char.draw(self.screen)

        pg.display.flip() # updates the screen
        self.clock.tick(72)  # Ограничиваем частоту обновления кадров

    def key_pressed(self) -> None:
        "pressed key"
        self.tvector = 0
        if self.key[pg.K_w]:
            self.tvector += -self.speed*1j
        if self.key[pg.K_s]:
            self.tvector += self.speed*1j
        if self.key[pg.K_a]:
            self.tvector += -self.speed
        if self.key[pg.K_d]:
            self.tvector += self.speed
        self.tvector = ns(self.tvector)
        self.inertia()
        self.pos += self.tvector

    @staticmethod
    def create_sprite(frames: list, k: float = 1.0) -> pg.sprite.Group:
        "creates a group of sprites from a given list of images"
        images = [pg.image.load(image).convert_alpha() for image in frames]
        if k!=1.0:
            images = [pg.transform.scale(image, (int(image.get_width() * k), int(image.get_height() * k))) for image in images]
        sprite = Sprite()
        sprite.set_sprite(images)
        return pg.sprite.Group(sprite)
    
    def inertia(self):
        self.dsc[0] = self.dsc[0][1:]+[self.tvector.real+self.tvector.imag*1j]
        self.dsc[1] = self.dsc[1][1:]+[sum(self.dsc[0])/len(self.dsc[0])]
        self.tvector = sum(self.dsc[1])/len(self.dsc[1])



if __name__ == "__main__":
    # import cProfile
    # cProfile.run("Game()", sort="cumulative")
    game = Game()
    pg.quit()
    sys.exit()
