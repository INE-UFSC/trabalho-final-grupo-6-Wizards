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


class Wind(Spell):
    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):

        image_dict = {"1": circle(50, (110, 0, 150))}
        sound_dict = {"casting": "wind_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Wind",
            icon=circle(Spell.icon_radius, (110, 0, 150)),
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            screen_size=screen_size,
            groups=groups,
        )
        self.kill()

    def cast(self, wiz):
        pass

    def update(self, dt):
        pass

    def colision(self, dt):
        pass
