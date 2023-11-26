import pygame as pg
import sys
import os
import json
# личные модули
from sprite import Sprite

# Задаём пути к папкам с изображениями через файл json
with open("frames.json", "r") as file:
    frames = json.load(file)
    IMG_DIR = "img"
    bg = os.path.join(IMG_DIR, "backgrounds", "bg.png")
    FIRE_IMAGES = [os.path.join(IMG_DIR, i) for i in frames["fire"]]
    ASTEROID_1 = [os.path.join(IMG_DIR, "asteroids", "asteroid_1.png")]
    ASTEROID_2 = [os.path.join(IMG_DIR, "asteroids", "asteroid_2.png")]
    ASTEROID_3 = [os.path.join(IMG_DIR, "asteroids", "asteroid_3.png")]
    ASTEROID_IMAGES = [os.path.join(IMG_DIR, i) for i in frames["asteroid"]]
    del IMG_DIR

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1400, 800))
        pg.display.set_caption("Jersey")
        self.running = True # Работа основного цикла игры
        self.clock = pg.time.Clock() # Экземпляр класса работы тиков
        self.tick = 0 # Тик на данный момент

        # Загружаем изображение фона
        self.bg = pg.image.load(bg).convert()
        # Создание спрайтов
        self.asteroid_sprite = self.create_sprite(ASTEROID_IMAGES)
        self.asteroid_sprite_1 = self.create_sprite(ASTEROID_1)
        self.fire_sprite = self.create_sprite(FIRE_IMAGES)
        self.pos = 0j # позиция основного игрока
        self.run() # Вызов основного игрового цикла

    def run(self):
        # Основной игровой цикл
        while self.running:
            self.tick += 1 if self.tick < 71 else -71
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        # Обработчик событий
        for event in pg.event.get():
            if event.type == pg.VIDEORESIZE:
                # Обработка изменения размера окна
                self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            elif event.type == pg.QUIT:
                self.running = False

    def update(self):
        # Отрисовка спрайтов
        for sprite in self.fire_sprite:
            sprite.update(self.tick, self.tick//24+1)
            sprite.move(complex(self.tick+500, 300), "topleft")

        for sprite in self.asteroid_sprite_1:
            sprite.update(self.tick, self.tick//24+1)
            sprite.move(complex(500, 400), "topright")

    def draw(self):
        # Рисуем фон
        self.screen.blit(self.bg, (0, 0))

        # Рисуем спрайты
        # Спрайты накладываются друг на друга
        self.asteroid_sprite_1.draw(self.screen)
        self.fire_sprite.draw(self.screen)

        pg.display.flip()
        self.clock.tick(72)  # Ограничиваем частоту обновления кадров

    @staticmethod
    def create_sprite(frames: list) -> pg.sprite.Group:
        images = [pg.image.load(image).convert_alpha() for image in frames]
        sprite = Sprite()
        sprite.set_sprite(images)
        return pg.sprite.Group(sprite)


if __name__ == "__main__":
    game = Game()
    pg.quit()
    sys.exit()