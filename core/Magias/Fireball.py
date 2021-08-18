import pygame as pg
from core.Magia import Magia
import time 

class Fireball(Magia):
    def __init__(self,grupo):
        Fireball_image = pg.Surface((100, 100), pg.SRCALPHA)
        pg.draw.circle(Fireball_image, (195, 48, 0), (20, 20), 20)
        super().__init__(nome="Fireball", icone = "fireball_icon",som = "fireball_sound",
                        radius=3, image_dict={"2":Fireball_image}, size=(20,20), ang=0,
                        vel=(0,0), groups=[grupo])
                     
        self.kill()


    def cast(self, mago): 
        self.__spawned_time = time.time()
        self.is_projectile = True  
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


