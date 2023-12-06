import pygame as pg
from configs.config import *
fps = game_config["fps"]


class Sprite(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.images = []  # list[list[pg.Surface]] list of sprites
        self.frame = 0  # index of active sprite
        self.length = {}  # int|dict number of sprites
        self.frames_ps = {}  # frames per second
        self.image = None  # active sprite
        self.rect = None # collision
        self.tick = 0

    def set_sprite(self, images: list) -> None:
        "Declaring sprites"
        self.images = images
        for i in range(len(self.images)):
            self.length[i] = len(self.images[i])
            self.frames_ps[i] = fps // self.length[i]
        if self.length == 0:  # Убрать, при конечной компиляции кода #C11
            raise ValueError("No images set. Call set_sprite method first.")
        self.image = self.images[0][self.frame]
        self.rect = self.image.get_rect(topleft=(0, 0))

    def update(self, index=0, rate=1) -> None:
        "Updating sprites"
        self.tick += 1 if self.tick < 71 else -71
        if self.tick % (self.frames_ps[index] // rate) == 0:
            self.frame = (self.frame + 1) % self.length[index]
            self.image = self.images[index][self.frame]

    def move(self, c: complex, position="topleft"):
        setattr(self.rect, position, (c.real, c.imag))
