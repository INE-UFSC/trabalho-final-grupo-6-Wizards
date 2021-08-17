import pygame as pg
from core.Magia import Magia
import time 

class Curse(Magia):
    def __init__(self,grupo):
        Curse_image = pg.Surface((20_0, 200), pg.SRCALPHA)
        pg.draw.circle(Curse_image, (150, 0, 150), (100, 100), 100)
        super().__init__(nome="Curse", icone = "curse_icon",som = "curse_sound",
                        radius=2, image_dict={"1":Curse_image}, size=(200,200), ang=0,
                        vel=(0,0), groups=[grupo])
        self.kill()

    def cast(self, mago): 
        self.__spawned_time = time.time()
        super().cast(mago)
      
    def update(self,dt):
        
        if time.time() > self.__spawned_time + 5:
            self.kill()
        super().update(1)

    def colisao(self):
      #if self.rect.colliderect()
        return super().colisao()