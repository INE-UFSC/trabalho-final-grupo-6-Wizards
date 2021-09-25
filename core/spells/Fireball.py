#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from images import circle
from core import Spell
from core.MathFuncions import dist_sq
import time
import os
import math


class Fireball(Spell):
    __projectile_duration = 1
    __area_duration = 0.25
    __abs_vel = 8
    R = 200

    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):

        # circle(7, (195, 48, 0)), "2": circle(100, (195, 48, 0))} tamanhos
        image_dict = {"1": {"path": os.path.join("images", "spells_img", "fireball_img.png"), "R": 7, "size": (16, 16)},
                      "2": {"path": os.path.join("images", "spells_img", "fireball_img_2.png"), "R": self.R, "size": (self.R*2+2, self.R*2+2)}}
        # "2": {"image": circle(self.R, (195, 48, 0))}}
        sound_dict = {"casting": "fireball_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Fireball",
            icon="fireball_icon",  # circle(Spell.icon_radius, (195, 48, 0)),
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            screen_size=screen_size,
            groups=groups,
        )

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
        self.__dmg_wiz = []

    def colision(self, wiz):
        # se atingir como projetil o tempo enquanto projetil acaba
        if self.is_projectile:
            if self.wizard_id == wiz.idx:
                return
            self.explosion()
        else:  # dano da explosão
            if not wiz.idx in self.__dmg_wiz:
                self.__dmg_wiz.append(wiz.idx)
                dist = math.sqrt(dist_sq(self.center, wiz.center))*5//self.R
                wiz.damage(5-dist)
