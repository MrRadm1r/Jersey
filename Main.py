import pygame as pg
# import numpy as np
import sys
import os
import json
from sprite import Sprite
# Задаем пути к папкам с изображениями
with open("frames.json", "r") as file:
    frames = json.load(file)
    IMG_DIR = "img"
    bg = os.path.join(IMG_DIR, "backgrounds", "bg.png")
    FIRE_IMAGES = [os.path.join(IMG_DIR, i) for i in frames["fire"]]
    ASTEROID_1 = [os.path.join(IMG_DIR, "asteroids", "asteroid_1.png")]
    ASTEROID_2 = [os.path.join(IMG_DIR, "asteroids", "asteroid_2.png")]
    ASTEROID_3 = [os.path.join(IMG_DIR, "asteroids", "asteroid_3.png")]
    D = [os.path.join(IMG_DIR, f"asteroid_{i}.png") for i in range(1, 4)]
    ASTEROID_IMAGES = [os.path.join(IMG_DIR, "asteroids", f"asteroid_{i}.png") for i in range(1, 4)]
    del IMG_DIR


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1400, 800))
        pg.display.set_caption("Jersey")

        # Загружаем изображение фона
        self.bg = pg.image.load(bg).convert()

        # Создание спрайта
        self.fire_sprite = self.create_sprite(FIRE_IMAGES)
        # self.asteroid_sprite = self.create_sprite(ASTEROID_IMAGES)
        self.asteroid_sprite_1 = self.create_sprite(ASTEROID_1)
        self.clock = pg.time.Clock()
        self.running = True
        self.tick = 0
        self.pos = 0j
        self.run()

    def run(self):
        while self.running:
            self.tick += 1 if self.tick <71 else -71
            print(self.tick)

            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                # Обработка события изменения размера окна
                self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            elif event.type == pg.QUIT:
                self.running = False

    def update(self):
        for sprite in self.fire_sprite:
            sprite.update(self.tick)
            sprite.move(complex(400, 300), "topleft")

        for sprite in self.asteroid_sprite_1:
            sprite.update(self.tick)
            sprite.move(complex(300, 400), "topright")
            

    def draw(self):
        # Рисуем фон
        self.screen.blit(self.bg, (0, 0))

        # Рисуем спрайты
        self.fire_sprite.draw(self.screen)
        self.asteroid_sprite_1.draw(self.screen)

        pg.display.flip()



        self.clock.tick(72)  # Ограничиваем частоту обновления кадров

    @staticmethod
    def create_sprite(frames: list):
        images = [pg.image.load(image).convert_alpha() for image in frames]
        return pg.sprite.Group(Sprite(images))


if __name__ == "__main__":
    game = Game()
    pg.quit()
    sys.exit()
