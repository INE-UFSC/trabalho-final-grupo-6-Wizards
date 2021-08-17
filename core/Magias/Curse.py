import pygame as pg
from core import Magia


class Curse(Magia):
    def __init__(self):
        super().__init__("Curse","curse_icon","curse_sound",2,{},(40,40),0)

    def cast(self, rect, **kwargs):
        print('vrummm')
        Curse_image = pg.Surface((20_0, 200), pg.SRCALPHA)
        pg.draw.circle(Curse_image, (255, 0, 255), (100, 100), 100)

