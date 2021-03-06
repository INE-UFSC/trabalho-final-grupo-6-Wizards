#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto

    Classe base para as magias
"""
from abc import ABC, abstractmethod
from core import GameObject, Wizard
from core import RSurface
import pygame as pg
import os
import time


class Spell(ABC, GameObject):
    icon_radius = 20

    def __init__(self, wizard_id: int, name: str, icon: str, image_dict: dict,
                 sound_dict: dict, ang: float, screen_size: tuple,
                 vel=(0, 0), groups=None):
        game_object_args = {"image_dict": image_dict, "sound_dict": sound_dict,
                            "ang": ang, "screen_size": screen_size, "vel": vel,
                            "groups": groups}

        super().__init__(**game_object_args)
        self.__name = name
        self.load_icon(icon)
        self.__wizard_id = wizard_id
        self.__spawned_time = 0
        self.__cast_sound = pg.mixer.Sound(
            os.path.join('sounds', 'spells', sound_dict["casting"]+".wav"))
        self.kill()

    @property
    def name(self):
        return self.__name

    @property
    def icon(self):
        return self.__icon

    @property
    def wizard_id(self):
        return self.__wizard_id

    @property
    def spawned_time(self):
        return self.__spawned_time

    def set_time(self):
        self.__spawned_time = time.time()

    def cast(self, wiz: Wizard):
        self.set_time()
        self.center = wiz.center
        self.__cast_sound.set_volume(1.0)
        self.__cast_sound.play()
        self.revive()

    @abstractmethod
    def colision(self):
        pass

    def load_icon(self, icon):
        icon = icon + ".png"

        image = pg.image.load(os.path.join(
            'images', 'spells_img', 'icons', icon))
        image.set_colorkey((255, 255, 255))
        image = image.convert_alpha()

        self.__icon = pg.transform.scale(image, (42, 42))


class SpellEffect(ABC):
    def __init__(self, duration: int, spell_type):
        self.__spawned_time = time.time()
        self.__duration = duration
        self.__spell_type = spell_type

    @property
    def spawned_time(self):
        return self.__spawned_time

    def renew(self):
        self.__spawned_time = time.time()

    @property
    def duration(self):
        return self.__duration

    @property
    def spell_type(self):
        return self.__spell_type

    def __call__(self, wiz):
        if time.time() > self.__spawned_time+self.__duration:
            wiz.effect_remove(self)
        else:
            self.call(wiz)

    @abstractmethod
    def call(self, wiz: Wizard):
        pass
