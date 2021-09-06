#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from images import circle
from core import Spell, SpellEffect, Wizard
import time


class Shield(Spell):
    __effect_duration = 2

    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):

        image_dict = {"1": circle(50, (0, 100, 0))}
        sound_dict = {"casting": "shield_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Shield",
            icon=circle(Spell.icon_radius, (0, 100, 0)),
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            screen_size=screen_size,
            groups=groups,
        )
        self.kill()

    def cast(self, wiz: Wizard):
        self.__wiz = wiz
        self.__wiz.shield = ShieldEffect(self.__effect_duration, self)
        super().cast(wiz)

    def update(self, dt):
        # magia tem duração de 2s
        if time.time() > self.spawned_time + self.__effect_duration:
            self.kill()
        center = self.__wiz.rect.center
        self.rect.update((center[0] - self.rect.size[0]/2,
                          center[1] - self.rect.size[1]/2),
                         self.rect.size)

    def colision(self, wiz):
        pass


class ShieldEffect(SpellEffect):
    def __init__(self, duration, orig_spell):
        super().__init__(duration, Shield)
        self.__spell = orig_spell
        self.__used = False

    def call(self, wiz):  # talvez implementar colisão
        if self.__used:
            wiz.effect_remove(self)
            wiz.shield = None
            self.__spell.kill()

    def block(self, damage):
        if not self.__used:
            self.__used = True
            return max(0, damage-2)
        else:
            return damage
