import pygame as pg
fps = 72

class Sprite(pg.sprite.Sprite):
    tick = 0
    def __init__(self, images: list):
        super().__init__()
        self.frame = 0
        self.images = images
        self.image = self.images[self.frame]
        self.lenght = len(self.images)
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.frames_ps = fps // self.lenght

    # def set_sprites(self, images: list):
    #     self.images = images
    #     self.image = self.images[self.frame]
    #     self.lenght = len(self.images)
    #     self.rect = self.image.get_rect(topleft=(0, 0))
    #     self.frames_ps = fps // self.lenght
    
    @staticmethod
    def set_tick(cls, tick):
        cls.tick += tick

    def update(self, ticks:int, rate=1):
        # tick: тик по счёту на данный момент
        # rate: количество циклов анимации на секунду (<= self.frames_ps)
        if ticks % (self.frames_ps // rate) == 0:
            self.frame = (self.frame + 1) % self.lenght
            self.image = self.images[self.frame]

    def move(self, c: complex, position="topleft"):
        setattr(self.rect, position, (c.real, c.imag))