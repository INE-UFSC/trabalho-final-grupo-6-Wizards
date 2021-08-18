import pygame as pg
from core.Magia import Magia
import time 

class Shield(Magia):
    def __init__(self,grupo):
        Shield_image = pg.Surface((100, 100), pg.SRCALPHA)
        pg.draw.circle(Shield_image, (110, 0, 150), (50, 50), 50)
        super().__init__(nome="Shield", icone = "shield_icon",som = "shield_sound",
                        radius=3, image_dict={"4":Shield_image}, size=(100,100), ang=0,
                        vel=(0,0), groups=[grupo])
        self.kill()

    def cast(self, mago): 
        self.__spawned_time = time.time()
        super().cast(mago)
      
    def update(self,dt):
        
        #magia tem duração de 2s
        if time.time() > self.__spawned_time + 2:
            self.kill()
        super().update(dt)

    def colisao(self, mago):
        pass

    