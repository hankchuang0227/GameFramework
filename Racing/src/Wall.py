import random

import pygame
import random
from mlgame.view.view_model import create_rect_view_data

peggy = ["#000000","#ffffff","#ff0000","#ffff00","#00ff00","#8c8c8c","#0000ff","#21A1F1","#00FFFF","#FF00FF","#282828","#646464","#643705"]
class Wall(pygame.sprite.Sprite):
    def __init__(self, init_pos: tuple, init_size: tuple):
        super().__init__()
        self.rect = pygame.Rect(*init_pos, *init_size)
        self.color = peggy[random.randint(0,11)]

    @property
    def xy(self):
        return self.rect.topleft

    @property
    def game_object_data(self):
        return create_rect_view_data(
            name="wall"
            , x=self.rect.x
            , y=self.rect.y
            , width=self.rect.width
            , height=self.rect.height
            , color=self.color
            , angle=0)








