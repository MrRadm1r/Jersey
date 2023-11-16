import pygame as pg

class Sprite(pg.sprite.Sprite):
    def __init__(self, surface, x: int|float, y: int|float, texture: str) -> None:
        pg.sprite.Sprite.__init__(self)
        self.texture = pg.image.load(texture).convert_alpha()
        self.rect = self.texture.get_rect(topleft=(x, y))
        surface.blit(self.texture, self.rect)
        
