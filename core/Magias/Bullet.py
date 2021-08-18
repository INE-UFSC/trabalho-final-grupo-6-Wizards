import pygame as pg
from core.Magia import Magia
import time


class Bullet(Magia):
    def __init__(self,grupo):
        self.__spawned_time = 0 
        self.__abs_vel = 5.0
        R = 7
        Bullet_image = pg.Surface((2*R, 2*R), pg.SRCALPHA)
        pg.draw.circle(Bullet_image, (100, 100, 255), (R, R), R)
        super().__init__(nome="Curse", icone = "curse_icon",som = "curse_sound",
                        radius=R, image_dict={"1":Bullet_image}, size=(2*R,2*R), ang=0,
                        vel=(0,0), groups=[grupo])
        self.kill()

    def cast(self, mago): 
        self.__spawned_time = time.time()
        super().cast(mago)
        
        self.vel = ( mago.angle_vector[0]*self.__abs_vel ,
                    mago.angle_vector[1]*self.__abs_vel)

    def update(self,dt):
        
        if time.time() > self.__spawned_time + 8:
            self.kill()
        super().update(1)
    


    def colisao(self):
        return super().colisao()      


