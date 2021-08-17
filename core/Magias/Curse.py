import pygame as pg
from core import Magia
class Curse(Magia):
    def __init__(self):
        super().__init__()

    def cast(self, rect, **kwargs):
        Mage_image = pg.Surface((200, 2000), pg.SRCALPHA)
        pg.draw.circle(Curse_image, (255, 0, 255), (100, 100), 100)

