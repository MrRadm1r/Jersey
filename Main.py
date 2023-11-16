import pygame as pg
import ctypes
from sprite import Sprite


class Jersey:
    pg.init()  
    def __init__(self) -> None:
        window = ctypes.windll.user32
        x = window.GetSystemMetrics(0)
        y = window.GetSystemMetrics(1)
        self.win = pg.display.set_mode((x, y)) # Настройка размера окна
        self.run = True
        self.fps = 60
        self.clock = pg.time.Clock()
        # Загрузка изображений
        self.bg = pg.image.load('img/bg.png').convert()
        # конец
        # Писать до
        self.game()


    def game(self) -> None:
        while self.run:
            

            self.drawon()
            # проверка ивентов
            for event in pg.event.get():
                if event.type == pg.QUIT: # Завершение программы
                    self.run = False
            self.clock.tick(self.fps)
        pg.quit()

    def drawon(self):
        self.win.blit(self.bg, (0, 0))
        Sprite(self.win, 0, 0, "img/asteroid_1.png")
        pg.display.update()


Jersey()