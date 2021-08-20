#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from images.circle import circle
from core import Spell, SpellEffect
import time


class Curse(Spell):
    __area_duration = 3
    __effect_duration = 2

    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):

        image_dict = {"1": circle(100, (150, 0, 150))}
        sound_dict = {"casting": "curse_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Curse",
            icon=circle(Spell.icon_radius, (150, 0, 150)),
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            screen_size=screen_size,
            groups=groups,
        )
        self.kill()

    def update(self, dt):
        if time.time() > self.spawned_time + self.__area_duration:
            self.kill()
        super().update(1)

    def colision(self, wiz):
        wiz.add_effect(CurseEffect(self.__effect_duration))


class CurseEffect(SpellEffect):
    def __init__(self, duration):
        super().__init__(duration, Curse)

    def call(self, wiz):
        wiz.accelerate()
