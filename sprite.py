import pygame as pg
fps = 72

class Sprite(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []  # list of sprites
        self.frame = 0  # index of active sprite
        self.length = 0  # number of sprites
        self.frames_ps = 0  # frames per second
        self.image = None  # active sprite
        self.rect = None  # collision

    def set_sprite(self, images: list):
        self.images = images
        self.length = len(self.images)
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.frames_ps = fps // self.length  # Пересчитываем frames_ps после установки images

    def update(self, tick, rate=1):
        if self.length == 0:
            raise ValueError("No images set. Call set_sprite method first.")
        
        if tick % (self.frames_ps // rate) == 0:
            self.frame = (self.frame + 1) % self.length
            self.image = self.images[self.frame]

    def move(self, c: complex, position="topleft"):
        setattr(self.rect, position, (c.real, c.imag))

