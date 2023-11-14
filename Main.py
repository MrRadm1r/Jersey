import ctypes
import time

import pygame


class Lazy_loading:
    pygame.init()

    def __init__(self, pattern):
        if not pattern:
            self.upload()

    def upload(self):
        pass


class Green_Paws:
    pygame.init()
    pygame.display.set_caption('Dandes')

    def __init__(self):
        window = ctypes.windll.user32
        self.x = window.GetSystemMetrics(0)
        self.y = window.GetSystemMetrics(1)
        self.win = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_icon(pygame.image.load('images/white.png').convert())
        self.run = True
        self.font = pygame.font.SysFont('Arial', 25)
        self.f_click = ()
        self.tile_size = 120
        self.obg = pygame.image.load('images/white.jpg').convert()
        self.bg = pygame.image.load('images/white.jpg').convert()
        self.bg = pygame.transform.scale(self.bg, (self.x, self.y))
        self.obg = pygame.transform.scale(self.bg, (self.x, self.y))
        self.bgs = self.bg.get_size()
        self.obgs = self.obg.get_size()
        self.bgx = self.x // 2 - self.bgs[0] // 2
        self.bgy = self.y // 2 - self.bgs[1] // 2
        self.zoom = 0.90
        self.tzoom = 1
        self.opts = ()
        self.a = time.time()
        self.b = 0
        self.lst = [1]

        self.game_events()

    def game_events(self):
        while self.run:
            self.drawon()
            self.event_detect()

            pygame.display.update()
        pygame.quit()

    def event_detect(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.display.iconify()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.MOUSEWHEEL:
                self.zooming(event.y)
        if mouse[2]:
            pygame.draw.rect(self.win, (100, 100, 100),
                             (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 200, 100))

    # def options(self, pressed):
    #     if not pressed:
    #         return
    #     else:
    #         self.

    def quit(self):
        self.run = False

    def drawon(self):
        self.dbg()
        self.win.blit(self.bg, (self.bgx, self.bgy))
        self.selection()
        if time.time() - self.a >= 1:
            self.lst.remove(1) if 1 in self.lst else 0
            self.lst.append(self.b)
            self.a = time.time()
            self.b = 0
        else:
            self.b += 1
        self.win.blit(
            self.font.render(
                f"примерный фпс: {sum(self.lst) // len(self.lst)}",
                True, 'red'), (0, 0))
        self.win.blit(
            self.font.render(
                f"максимальный фпс: {max(self.lst)}",
                True, 'red'), (0, 22))
        self.win.blit(
            self.font.render(
                f"минимальный фпс: {min(self.lst)}",
                True, 'red'), (0, 44))
        self.win.blit(
            self.font.render(
                f"фпс: {self.lst[-1]}",
                True, 'red'), (0, 66))

    def zooming(self, scroll_side):
        if scroll_side == 1:
            self.tzoom /= self.zoom

        if scroll_side == -1 and self.tzoom * self.zoom >= 1:
            self.tzoom *= self.zoom

        temp = (self.obgs[0] * self.tzoom, self.obgs[1] * self.tzoom)
        df = [(self.bg.get_rect().center[i] - pygame.mouse.get_pos()[i]) * self.zoom for i in range(2)]
        self.bg = pygame.transform.scale(self.obg, temp)
        self.bgs = self.bg.get_size()
        self.bgx = (self.x - self.bgs[0]) // 2 + df[0]
        self.bgy = (self.y - self.bgs[1]) // 2 + df[1]

    def selection(self):
        if pygame.mouse.get_pressed()[0]:
            if self.f_click:
                pass
            else:
                self.f_click = pygame.mouse.get_pos()
            x1 = self.f_click[0]
            y1 = self.f_click[1]
            x2 = pygame.mouse.get_pos()[0]
            y2 = pygame.mouse.get_pos()[1]
            self.arect(self.win, (164, 202, 255, 80), (min(x1, x2), min(y1, y2),
                                                       max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)))
            pygame.draw.line(self.win, (40, 40, 125, 90), (x1, y1), (x1, y2))
            pygame.draw.line(self.win, (40, 40, 125, 90), (x1, y1), (x2, y1))
            pygame.draw.line(self.win, (40, 40, 125, 90), (x1, y2), (x2, y2))
            pygame.draw.line(self.win, (40, 40, 125, 90), (x2, y1), (x2, y2))
            return self.f_click + (pygame.mouse.get_pos())
        self.f_click = ()
        return ''

    @staticmethod
    def arect(surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)

    def dbg(self):
        if self.bgx > 0:
            # self.bgx = (0, self.bgs[1])
            self.bgx = 0
        if self.bgy > 0:
            # self.bgs = (self.bgs[0], 0)
            self.bgy = 0


attemp = open('attemps.txt', 'r+', encoding="utf-8").read()
file = open('attemps.txt', 'w', encoding="utf-8")
file.write(str(int(attemp) + 1))
file.close()

if __name__ == '__main__':
    Green_Paws()
