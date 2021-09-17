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
import os


class Teleport(Spell):
    __dist = 400
    __image_duration = 0.5
    __effect_duration = 1

    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):

        image_dict = {"1": {"path": os.path.join(
            "images", "spells_img", "teleport_img.png"), "R": 25, "size": (52, 52)}}
        sound_dict = {"casting": "teleport_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Teleport",
            icon="teleport_icon",
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            screen_size=screen_size,
            groups=groups,
        )
        self.kill()

    def cast(self, wiz):
        super().cast(wiz)
        # move automaticamente a determinada distancia
        dist = (wiz.angle_vector[0] * self.__dist + self.center[0],
                wiz.angle_vector[1] * self.__dist + self.center[1])
        dist = (dist[0] % self.screen_size[0], dist[1] % self.screen_size[1])
        wiz.center = dist

    def update(self, dt):
        # magia tem duração de 2s
        if time.time() > self.spawned_time + self.__effect_duration:
            self.kill()
        super().update(dt)

    def colision(self, wiz):
        pass
