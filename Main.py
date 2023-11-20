import pygame as pg
import numpy as np
import sys
import os
from sprite import Sprite
# Задаем пути к папкам с изображениями
IMG_DIR = "img"
bg = os.path.join(IMG_DIR, "bg.png")
FIRE_IMAGES = [os.path.join(IMG_DIR, "fire", f"fire{i}.png") for i in range(1, 4)]
ASTEROID_IMAGES = [os.path.join(IMG_DIR, f"asteroid_{i}.png") for i in range(1, 4)]

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1400, 800))
        pg.display.set_caption("Jersey")

        # Загружаем изображение фона
        self.bg = pg.image.load(bg).convert()

        # Создание спрайта
        self.fire_sprite = self.create_sprite(FIRE_IMAGES)
        self.asteroid_sprite = self.create_sprite(ASTEROID_IMAGES)
        self.clock = pg.time.Clock()
        self.running = True
        self.tick = 0
        self.run()

    def run(self):
        while self.running:
            if self.tick < 71:
                self.tick += 1
            else:
                self.tick = 0
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

        for sprite in self.asteroid_sprite:
            sprite.update(self.tick)
            sprite.move(complex(300, 400), "topright")
            

    def draw(self):
        # Рисуем фон
        self.screen.blit(self.bg, (0, 0))

        # Рисуем спрайты
        self.fire_sprite.draw(self.screen)
        self.asteroid_sprite.draw(self.screen)

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
