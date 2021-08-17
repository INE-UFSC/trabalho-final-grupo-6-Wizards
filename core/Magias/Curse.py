import pygame as pg
from core.Magia import Magia


class Curse(Magia):
    def __init__(self,grupo):
        Curse_image = pg.Surface((20_0, 200), pg.SRCALPHA)
        pg.draw.circle(Curse_image, (255, 0, 255), (100, 100), 100)
        super().__init__(nome="Curse", icone = "curse_icon",som = "curse_sound",
                        radius=2, image_dict={"1":Curse_image}, size=(200,200), ang=0,
                        vel=(0,0), groups=[grupo])
        self.kill()

    def cast(self, rect, **kwargs):
        self.rect.update(rect)
        print('vrummm')
        self.revive()
        Curse_image = pg.Surface((200, 200), pg.SRCALPHA)
        pg.draw.circle(Curse_image, (255, 0, 255), (100, 100), 100)

    def colisao(self):
        return super().colisao()