import pygame as pg
from core.Magia import Magia


class Bullet(Magia):
    def __init__(self,grupo):
        self.__abs_vel = 2.0
        R = 7
        Bullet_image = pg.Surface((2*R, 2*R), pg.SRCALPHA)
        pg.draw.circle(Bullet_image, (100, 100, 255), (R, R), R)
        super().__init__(nome="Curse", icone = "curse_icon",som = "curse_sound",
                        radius=R, image_dict={"1":Bullet_image}, size=(2*R,2*R), ang=0,
                        vel=(0,0), groups=[grupo])
        self.kill()

    def cast(self, mago): 
        super().cast(mago)
        
        self.vel = ( mago.angle_vector[0]*self.__abs_vel ,
                    mago.angle_vector[1]*self.__abs_vel)
    def colisao(self):
      #if self.rect.colliderect()
        return super().colisao()      


