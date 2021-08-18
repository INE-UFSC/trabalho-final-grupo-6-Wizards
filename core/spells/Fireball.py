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


class Fireball(Spell):
    __projectile_duration = 2
    __area_duration = 0.25

    def __init__(self, wizard_id: int, groups: list):
        self.is_projectile = True

        image_dict = {"1": circle(7, (195, 48, 0)),
                      "2": circle(50, (195, 48, 0))}
        sound_dict = {"casting": "fireball_sound"}

        super().__init__(wizard_id=wizard_id, name="Fireball", icon="fireball_icon",
                         image_dict=image_dict, sound_dict=sound_dict, ang=0,
                         groups=groups)
        self.kill()

    def cast(self, wiz):
        self.__spawned_time = time.time()

        self.vel = (wiz.angle_vector[0]*self.__abs_vel,
                    wiz.angle_vector[1]*self.__abs_vel)
        super().cast(wiz)

    def update(self, dt):
        super().update(dt)
        now = time.time()

        if self.is_projectile:
            if now > self.__spawned_time + 3:
                self.__spawned_time = now
                self.is_projectile = False
        else:
            if now > self.__spawned_time + 0.25:
                self.kill()

    def colisao(self, wiz):
        # se atingir como projetil o tempo enquanto projetil acaba
        if self.is_projectile:
            self.__spawned_time = time.time()
            self.is_projectile = False
        else:  # dano da explosão
            wiz.damage(5)
