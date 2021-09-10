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
import time
import pygame as pg
import os


class Bullet(Spell):
    __projectile_duration = 8
    __abs_vel = 5
    __damge = 2

    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):
        image_dict = {"1": {"path": os.path.join(
            ["images", "spells_img", "bullet_img.png"]), "R": 7, "size": (16, 16)}}

        sound_dict = {"casting": "bullet_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Bullet",
            icon=circle(Spell.icon_radius, (100, 100, 255)),
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

    def update(self, dt):
        if time.time() > self.spawned_time + self.__projectile_duration:
            self.kill()
        super().update(1)

    def colision(self, wiz):
        if wiz.idx != self.wizard_id:
            wiz.damage(self.__damge)
            self.kill()
