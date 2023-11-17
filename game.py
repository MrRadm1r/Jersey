import pygame as pg
import sys
import os

# Задаем пути к папкам с изображениями
IMG_DIR = "img"
bg = os.path.join(IMG_DIR, "bg.png")
ASTEROID_IMAGES = [os.path.join(IMG_DIR, f"asteroid_{i}.png") for i in range(1, 4)]


class Sprites(pg.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.frame = 0
        self.images = images
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.animation_timer = 0

    def update(self, ticks):
        if ticks % 24 == 0:
            self.frame = (self.frame + 1) % len(self.images)
            self.image = self.images[self.frame]

    def move(self, c: complex, position="topleft"):
        setattr(self.rect, position, (c.real, c.imag))


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
        pg.display.set_caption("Jersey")

        # Загружаем изображение фона
        self.background = pg.image.load(bg).convert()

        # Загружаем изображения спрайтов
        asteroid_images = [pg.image.load(image).convert_alpha() for image in ASTEROID_IMAGES]

        # Передаем начальные координаты и изображения для создания спрайта
        self.sprites = pg.sprite.Group(Sprites(asteroid_images))
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
        self.sprites.draw(self.screen)

        pg.display.flip()

    def update(self):
        for sprite in self.sprites:
            sprite.update(self.tick)
            sprite.move(complex(400, 300), "center")

        self.clock.tick(72)  # Ограничиваем частоту обновления кадров


if __name__ == "__main__":
    game = Game()
    pg.quit()
    sys.exit()
