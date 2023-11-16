import pygame as pg
import sys
import os

# Задаем пути к папкам с изображениями
IMG_DIR = "img"
bg = os.path.join(IMG_DIR, "bg.png")
ASTEROID_IMAGES = [os.path.join(IMG_DIR, f"asteroid_{i}.png") for i in range(1, 4)]


class Sprites(pg.sprite.Sprite):
    def __init__(self, initial_position, images):
        super().__init__()
        self.image_index = 0
        self.images = images
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(topleft=initial_position)
        self.animation_timer = 0

    def update(self, clock):
        # Переключаем изображение каждые 6 кадров
        # elapsed_time = clock.tick(60)  # Получаем время, прошедшее с предыдущего кадра
        # if elapsed_time > 0:
        #     frame_time = elapsed_time / 1000.0  # Переводим в секунды
        #     if pg.time.get_ticks() - self.animation_timer > 6 * frame_time * 1000:
        #         self.image_index = (self.image_index + 1) % len(self.images)
        #         self.image = self.images[self.image_index]
        #         self.animation_timer = pg.time.get_ticks()
        self.image = self.images[clock]


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
        initial_position = (400, 300)
        self.sprites = pg.sprite.Group(Sprites(initial_position, asteroid_images))
        self.clock = pg.time.Clock()
        self.running = True
        self.tick = 0


        self.run()

    def run(self):
        while self.running:
            if self.tick<59:
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
            print(self.tick//20)
            sprite.update(self.tick//20)
            sprite.rect.x = self.tick//30  # Двигаем спрайт влево на 1 пиксель при каждом обновлении


if __name__ == "__main__":
    game = Game()
    pg.quit()
    sys.exit()
