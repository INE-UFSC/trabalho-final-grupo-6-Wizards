#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from images.circle import circle
from core import Spell
import time


class Teleport(Spell):
    __dist = 300
    __image_duration = 0.5

    def __init__(self, wizard_id: int, groups: list):

        image_dict = {"1": circle(50, (110, 0, 150))}
        sound_dict = {"casting": "teleport_sound"}

        super().__init__(wizard_id=wizard_id, name="Teleport", icon="Teleport_icon",
                         image_dict=image_dict, sound_dict=sound_dict, ang=0,
                         groups=groups)
        self.kill()

    def cast(self, wiz, dt):
        # move automaticamente a determinada distancia
        dist = (wiz.angle_vector[0]*self.__dist,
                wiz.angle_vector[1]*self.__dist)
        wiz.rect.move_ip(*dist)

    def update(self, dt):
        # magia tem duração de 2s
        if time.time() > self.__spawned_time + self.__effect_duration:
            self.kill()
        super().update(dt)

    def colision(self):
        pass
