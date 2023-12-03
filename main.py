import pygame as pg
import sys
import os
import json
# личные модули
from libs.sprite import Sprite
from libs.movement import *

def full_path(path_key: str) -> list[list[str]]:
    "takes paths of sprites from json file by key"
    IMG_DIR = "img"
    return [[os.path.join(IMG_DIR, path) for path in i] for i in frames[path_key]]

# Задаём пути к папкам с изображениями через файл json
with open("frames.json", "r") as file:
    frames = json.load(file)
    bg = os.path.join("img", "backgrounds", "bg.png")
    MAIN_CHAR = full_path("main_character")
    ASTEROID_1 = full_path("asteroid_1")

class Game:
    def __init__(self) -> None:
        pg.init() # инициализация пайгейм на всякий пожарный
        self.w = 1400
        self.h = 800
        self.speed = 8
        self.l = 15
        self.dsc = [[0j]*self.l]*2
        self.screen = pg.display.set_mode((self.w, self.h), pg.RESIZABLE)
        pg.display.set_caption("Jersey")
        self.running = True # Работа основного цикла игры
        self.clock = pg.time.Clock() # Экземпляр класса работы тиков
        self.tick = 0 # Тик на данный момент
        # Загружаем изображение фона
        self.bg = pg.image.load(bg).convert()
        # Создание спрайтов
        self.asteroid_sprite_1 = self.create_sprite(ASTEROID_1, mode=1)
        self.main_char = self.create_sprite(MAIN_CHAR, 0.15, mode=1)
        self.pos = self.w*0.5+self.h*0.5j # позиция основного игрока
        self.tvector = 0
        self.fps = []
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
            sprite.char_update(self.tick)
            sprite.move(complex(0, 400), "topleft")

        for sprite in self.main_char:
            sprite.char_update(self.tick, index=0, rate=2.5)
            sprite.move(self.pos, "center")

    def draw(self) -> None:
        "draws on the screen"
        self.screen.blit(self.bg, (0, 0)) # Рисуем Фон

        # Рисуем спрайты
        self.asteroid_sprite_1.draw(self.screen)
        self.main_char.draw(self.screen)

        pg.display.flip() # updates the screen
        self.clock.tick(72)  # Ограничиваем частоту обновления кадров

    def key_pressed(self) -> None:
        "pressed key"
        self.tvector = 0
        if self.key[pg.K_w]: self.tvector += -self.speed*1j
        if self.key[pg.K_s]: self.tvector += self.speed*1j
        if self.key[pg.K_a]: self.tvector += -self.speed
        if self.key[pg.K_d]: self.tvector += self.speed
        self.tvector = ns(self.tvector)
        self.tvector = inertia(self.tvector)
        self.pos += self.tvector

    @staticmethod
    def create_sprite(frames, k: float = 1.0, mode=0) -> pg.sprite.Group:
        "creates a group of sprites from a given list of images"
        if not mode:  # Надо постараться удалить это
            images = [pg.image.load(image).convert_alpha() for image in frames]
            if k!=1.0:
                images = [pg.transform.scale(image, (int(image.get_width() * k), int(image.get_height() * k))) for image in images]
            sprite = Sprite()
            sprite.set_char_sprite(images)
            return pg.sprite.Group(sprite)
        else:
            images = [[pg.image.load(image) for image in i] for i in frames]
            if k==1.0:
                pass
            else:
                images = [[pg.transform.scale(image, (int(image.get_width() * k), int(image.get_height() * k))) for image in i] for i in images]
            sprite = Sprite()
            sprite.set_char_sprite(images)
            return pg.sprite.Group(sprite)


if __name__ == "__main__":
    # import cProfile
    # cProfile.run("Game()", sort="cumulative")
    game = Game()
    pg.quit()
    sys.exit()
