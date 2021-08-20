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


class Wind(Spell):
    def __init__(self, wizard_id: int, groups: list):

        image_dict = {"1": circle(50, (110, 0, 150))}
        sound_dict = {"casting": "wind_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Wind",
            icon=circle(10, (110, 0, 150)),
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            groups=groups,
        )
        self.kill()

    def cast(self, wiz):
        pass

    def update(self, dt):
        pass

    def colision(self, dt):
        pass
