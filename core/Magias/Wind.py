import pygame as pg
from core.Magia import Magia

class Wind(Magia):
    def __init___(self, grupo):
        Wind_image = pg.Surface((100, 100), pg.SRCALPHA)
        pg.draw.circle(Wind_image, (0, 0, 150), (50, 50), 50)
        super().__init__(nome="Wind", icone = "Wind_icon",som = "Wind_sound",
                        radius=3, image_dict={"5":Wind_image}, size=(100,100), ang=0,
                        vel=(0,0), groups=[grupo])
        self.kill()

    def cast(self, mago): 
        pass
