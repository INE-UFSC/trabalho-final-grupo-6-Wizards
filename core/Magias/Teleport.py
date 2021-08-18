import pygame as pg
from core.Magia import Magia

class Teleport(Magia):
    def __init__(self, grupo):
        super().__init__(nome="Teleport", icone = "Teleport_icon",som = "Teleport_sound",
                        radius=3, image_dict={"5":Teleport_image}, size=(100,100), ang=0,
                        vel=(0,0), groups=[grupo])

        self.dist = 300
        self.kill()

    def cast(self, mago, dt):
        #move automaticamente a determinada distancia
        dist = ( mago.angle_vector[0]*self.dist ,
                    mago.angle_vector[1]*self.distl)
        mago.rect.move_ip(*dist)

    def update(self):
        pass

    def colisao(self):
        pass