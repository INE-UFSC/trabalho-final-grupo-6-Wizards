#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from images import circle
from core import Spell, SpellEffect
from core.MathFuncions import calc_angle
import time
import os
import math


class Wind(Spell):
    __hitbox_duration = 100
    __force = 25
    R = 200

    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):

        image_dict = {"1": {"path": os.path.join(
            "images", "spells_img", "wind_img.png"), "R": self.R, "size": (
            self.R*2+2, self.R*2+2)}}
        sound_dict = {"casting": "wind_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Wind",
            icon="wind_icon",
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            screen_size=screen_size,
            groups=groups,
        )
        self.kill()

    def cast(self, wiz):
        self.__affected_wiz = [self.wizard_id]
        super().cast(wiz)
        self.ang = wiz.ang
        new_center = (wiz.center[0] + wiz.angle_vector[0]*15,
                      wiz.center[1] + wiz.angle_vector[1]*15)
        self.center = wiz.center

    def update(self, dt):
        if time.time() > self.spawned_time + self.__hitbox_duration:
            self.kill()
        super().update(1)

    def colision(self, wiz):
        if wiz.idx not in self.__affected_wiz:
            wiz_ang = calc_angle(wiz.center[0] - self.center[0],
                                 wiz.center[1] - self.center[1])

            ang_dif = (wiz_ang - self.ang) % 360
            if ang_dif <= 45 or ang_dif >= 315:
                self.__affected_wiz.append(wiz.idx)
                ang = math.radians(wiz_ang)
                angle_vector = (math.cos(ang), -math.sin(ang))
                wiz.vel = (wiz.vel[0] + self.__force * angle_vector[0],
                           wiz.vel[1] + self.__force * angle_vector[1])
                wiz.damage(1)


class WindEffect(SpellEffect):
    __force = 5

    def __init__(self, duration, direction):
        super().__init__(duration, Wind)
        self.direction = direction

    def call(self, wiz):
        wiz.vel = (wiz.vel[0] + self.__force * self.direction[0],
                   wiz.vel[1] + self.__force * self.direction[1])
