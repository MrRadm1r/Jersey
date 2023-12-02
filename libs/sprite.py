import pygame as pg
fps = 72


class Sprite(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []  # list of sprites
        self.char_images = []  # list of character sprites EX
        self.frame = 0  # index of active sprite
        self.length = 0  # number of sprites
        self.char_length = {}  # number of sprites EX
        self.frames_ps = 0  # frames per second
        self.char_frames_ps = dict()  # frames per second EX
        self.image = None  # active sprite
        self.rect = None  # collision

    def set_sprite(self, images: list):
        self.images = images
        self.length = len(self.images)
        if self.length == 0:  # Убрать, при конечной компиляции кода #C11
            raise ValueError("No images set. Call set_sprite method first.")
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.frames_ps = fps // self.length  # Пересчитываем frames_ps после установки images

    def update(self, tick, rate=1) -> None:
        "Обновление спрайтов"
        if tick % (self.frames_ps // rate) == 0:
            self.frame = (self.frame + 1) % self.length
            self.image = self.images[self.frame]

    def set_char_sprite(self, images: list): # EX
        self.char_images = images
        for i in range(len(self.char_images)):
            self.char_length[i] = len(self.char_images[i])
            self.char_frames_ps[i] = fps // self.char_length[i]
            print(self.char_images[i])
        if self.char_length == 0:  # Убрать, при конечной компиляции кода #C11
            raise ValueError("No images set. Call set_sprite method first.")
        self.image = self.char_images[0][self.frame]
        self.rect = self.image.get_rect(topleft=(0, 0))

    def char_update(self, tick, index=0, rate=1): # EX
        "Обновление спрайтов сущностей"
        if tick % (self.char_frames_ps[index] // rate) == 0:
            self.frame = (self.frame + 1) % self.char_length[index]
            # print(index, self.frame)
            self.image = self.char_images[index][self.frame]

    def move(self, c: complex, position="topleft"):
        setattr(self.rect, position, (c.real, c.imag))
