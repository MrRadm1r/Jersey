# main.py
import pygame as pg
import sys
import os
from sprites import Sprite

# Задаем пути к папкам с изображениями
IMG_DIR = "img"
bg = os.path.join(IMG_DIR, "bg.png")
FIRE_IMAGES = [os.path.join(IMG_DIR, "fire", f"fire{i}.png") for i in range(1, 4)]
ASTEROID_IMAGES = [os.path.join(IMG_DIR, f"asteroid_{i}.png") for i in range(1, 4)]

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
        pg.display.set_caption("Jersey")

        # Загружаем изображение фона
        self.background = pg.image.load(bg).convert()

        # Cоздания спрайта
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
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.VIDEORESIZE:
                # Обработка события изменения размера окна
                self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

    def draw(self):
        # Рисуем фон
        self.screen.blit(self.background, (0, 0))

        # Рисуем спрайты
        self.fire_sprite.draw(self.screen)
        self.asteroid_sprite.draw(self.screen)

        pg.display.flip()

    def update(self):
        for fire_sprite in self.fire_sprite:
            fire_sprite.update(self.tick)
            fire_sprite.move(complex(400, 300), "topleft")

        for asteroid_sprite in self.asteroid_sprite:
            asteroid_sprite.update(self.tick)
            asteroid_sprite.move(complex(300, 400), "topright")

        self.clock.tick(72)  # Ограничиваем частоту обновления кадров

    @staticmethod
    def create_sprite(frames: list):
        images = [pg.image.load(image).convert_alpha() for image in frames]
        return pg.sprite.Group(Sprite(images))


if __name__ == "__main__":
    game = Game()
    pg.quit()
    sys.exit()
