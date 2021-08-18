import pygame as pg
from core.Magia import Magia
import time


class Curse(Magia):
    def __init__(self, grupo):
        Curse_image = pg.Surface((200, 200), pg.SRCALPHA)
        pg.draw.circle(Curse_image, (150, 0, 150), (100, 100), 100)
        super().__init__(nome="Curse", icone="curse_icon", som="curse_sound",
                         radius=100, image_dict={"1": Curse_image},
                         size=(200, 200), ang=0, vel=(0, 0), groups=[grupo])
        self.kill()

    def cast(self, mago):
        self.__spawned_time = time.time()
        super().cast(mago)

    def update(self, dt):
        if time.time() > self.__spawned_time + 50:
            self.kill()
        super().update(1)

    def colisao(self, mago):
        mago.add_effect(CurseEffect())


class CurseEffect():
    def __init__(self):
        self.__spawned_time = time.time()

    def __call__(self, mago):
        if time.time() > self.__spawned_time+2:
            mago.effect_remove(self)
        else:
            mago.accelerate()
