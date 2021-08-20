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
    __projectile_duration = 1
    __area_duration = 0.25
    __abs_vel = 5

    def __init__(self, wizard_id: int, groups: list):

        image_dict = {"1": circle(7, (195, 48, 0)), "2": circle(50, (195, 48, 0))}
        sound_dict = {"casting": "fireball_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Fireball",
            icon=circle(10, (195, 48, 0)),
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            groups=groups,
        )
        self.kill()

    def cast(self, wiz):
        super().cast(wiz)
        self.vel = (
            wiz.angle_vector[0] * self.__abs_vel,
            wiz.angle_vector[1] * self.__abs_vel,
        )
        self.is_projectile = True
        self.state = "1"

    def update(self, dt):

        super().update(dt)
        now = time.time()

        if self.is_projectile:
            if now > self.spawned_time + self.__projectile_duration:
                self.explosion()
        else:
            if now > self.spawned_time + self.__area_duration:
                self.kill()

    def explosion(self):  # comportamento quando a bola de fogo passa a explodir
        self.set_time()
        self.is_projectile = False
        self.state = "2"  # estado 2 = explodindo
        self.vel = (0, 0)  # parar a fireball

    def colision(self, wiz):
        if self.wizard_id == wiz.idx:
            return
        # se atingir como projetil o tempo enquanto projetil acaba
        if self.is_projectile:
            self.explosion()
        else:  # dano da explosão
            wiz.damage(5)
