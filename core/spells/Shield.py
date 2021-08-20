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


class Shield(Spell):
    __effect_duration = 2

    def __init__(self, wizard_id: int, groups: list):

        image_dict = {"1": circle(50, (0, 100, 0))}
        sound_dict = {"casting": "shield_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Shield",
            icon=circle(10, (0, 100, 0)),
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            groups=groups,
        )
        self.kill()

    def update(self, dt):
        # magia tem duração de 2s
        if time.time() > self.spawned_time + self.__effect_duration:
            self.kill()
        super().update(dt)

    def colision(self, wiz):
        pass


class ShieldEffect(SpellEffect):
    def __init__(self, duration):
        super().__init__(duration, Shield)

    def call(self, wiz):
        wiz.accelerate()
