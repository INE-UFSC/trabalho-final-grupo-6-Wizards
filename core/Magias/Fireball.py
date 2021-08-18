import pygame as pg
from core.Magia import Magia
import time 

class Fireball(Magia):
    def __init__(self,grupo):
        self.is_projectile = True
        Fireball_image = pg.Surface((14, 14), pg.SRCALPHA)
        pg.draw.circle(Fireball_image, (195, 48, 0), (7, 7), 7)
        Fireball_explosion_image = pg.Surface((100, 100), pg.SRCALPHA)
        pg.draw.circle(Fireball_explosion_image, (195, 48, 0), (50, 50), 50)
        image_dict ={"2":Fireball_image, "3":Fireball_explosion_image}
        super().__init__(nome="Fireball", icone = "fireball_icon",som = "fireball_sound",
                        radius=3, image_dict=image_dict, size=(50,50), ang=0,
                        vel=(0,0), groups=[grupo])
                     
        self.kill()


    def cast(self, mago): 
        self.__spawned_time = time.time()
        
        self.vel = ( mago.angle_vector[0]*self.__abs_vel ,
                    mago.angle_vector[1]*self.__abs_vel)  
        super().cast(mago)

    def update(self,dt):
        super().update(dt)
        now = time.time()

        if self.is_projectile:
            if now > self.__spawned_time + 3:
                self.__spawned_time = now
                self.is_projectile = False
        else:
            if now > self.__spawned_time + 0.25:
                self.kill()



    def colisao(self, mago):

        #se atingir como projetil o tempo enquanto projetil acaba
        if self.is_projectile:
            self.__spawned_time = time.time()
            self.is_projectile = False
        else:
        #dano da explosão
            mago.damage(5)


