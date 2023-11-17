import pygame as pg

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