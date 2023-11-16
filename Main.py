import pygame as pg
import ctypes
import pygame

window = ctypes.windll.user32
x = window.GetSystemMetrics(0) * 0.55
y = window.GetSystemMetrics(1) * 0.55

class Jersey:
    def __init__(self) -> None:
        pygame.init()  
        window = ctypes.windll.user32
        x = window.GetSystemMetrics(0) * 0.55
        y = window.GetSystemMetrics(1) * 0.55
        self.win = pg.display.set_mode((x, y)) 
        self.posx = 50
        self.posy = 50   
        self.width = 40 
        self.height = 60  
        self.speed = 4 
        self.run = True
        self.game()
    def game(self):
        while self.run:
            pygame.time.delay(50)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            self.win.fill((0,0,0))
            pygame.draw.rect(self.win, (123, 123, 255), (self.posx, self.posy, self.width, self.height))
            pygame.display.update()
        pygame.quit()


Jersey()