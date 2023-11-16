import pygame as pg
import ctypes
import pygame

window = ctypes.windll.user32
x = window.GetSystemMetrics(0) * 0.55
y = window.GetSystemMetrics(1) * 0.55


class Green_Paws:
    def init(self):
        pygame.init()
        self.win = pg.display.set_mode((x, y))
        pg.display.set_caption('alpha:1.0')
        # pg.display.set_icon(pg.image.load(''))
        self.posx = 50
        self.posy = 50
        self.width = 40
        self.height = 60
        self.speed = 4
        self.run = True

        self.game_events()

    def game_events(self):
        while self.run:
            pygame.time.delay(50)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
            self.press_key()
            self.win.fill((0,0,0))
            pygame.draw.rect(self.win, (123, 123, 255), (self.posx, self.posy, self.width, self.height))
            pygame.display.update()
        pygame.quit()
    def press_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.posx -= self.speed
        if keys[pygame.K_RIGHT]:
            self.posx += self.speed
        if keys[pygame.K_UP]:
            self.posy -= self.speed
        if keys[pygame.K_DOWN]:
            self.posy += self.speed


Green_Paws()