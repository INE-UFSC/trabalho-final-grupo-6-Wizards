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
import time
import os


class Wind(Spell):

    __effect_duration = 1
    R = 100

    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):

        image_dict = {"1": {"path": os.path.join(
            "images", "spells_img", "curse_img.png"), "R": self.R, "size": (
            self.R*2+2, self.R*2+2)}}
        sound_dict = {"casting": "teleport_sound"}

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
        super().cast(wiz)
        self.direction = wiz.angle_vector
        new_center = (self.center[0] + wiz.angle_vector[0]
                      * self.R + 55, self.center[1] + wiz.angle_vector[1] * self.R + 55)
        self.center = new_center

    def update(self, dt):
        if time.time() > self.spawned_time + self.__effect_duration:
            self.kill()
        super().update(1)

    def colision(self, wiz):
        wiz.add_effect(WindEffect(self.__effect_duration, self.direction))


class WindEffect(SpellEffect):
    def __init__(self, duration, direction):
        super().__init__(duration, Wind)
        self.direction = direction

    def call(self, wiz):
        wiz.accelerate()
        wiz.vel = (wiz.vel[0] + 20 * self.direction[0],
                   wiz.vel[1] + 20 * self.direction[1])
