#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
# from hashlib import new
# from sys import displayhook
from core import GameObject
import random
import time


class Wizard(GameObject):
    def __init__(self, idx: int, max_life: int, spell_list: list,
                 base_damage: int, ang: float, groups: list, Image_dict: dict,
                 sound_dict: dict, acc_ang=5, accel=0.5, atr=0.99):
        self.__idx = idx
        self.__max_life = max_life
        self.__spell_list = spell_list
        self.__base_damage = base_damage
        self.__accel = accel
        self.__life = max_life
        self.__slots = [None, None, None]
        self.__effects = []
        self.__atr = atr
        self.__cooldown = 1
        super().__init__(image_dict=Image_dict, sound_dict=sound_dict,
                         ang=ang, vel=(0, 0), groups=groups)
        self.__alive = True
        self.__impulse = False
        self.__acc_ang = acc_ang
        self.__vel_ang = 5
        self.__rotating = False
        self.__clockwise = False
        self.calc_angle_vector()

        for x in range(3):
            self.slots[x] = random.choice(self.spell_list)
            self.spell_list.remove(self.slots[x])

        self.__spell_list = [self.slots[1]]
        self.delay = [3, 3, 3]

    @property
    def idx(self):
        return self.__idx

    @property
    def max_life(self):
        return self.__max_life

    @property
    def spell_list(self):
        return self.__spell_list

    @property
    def base_damage(self):
        return self.__base_damage

    @property
    def accel(self):
        return self.__accel

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, life: int):
        self._life = life

    @property
    def slots(self):
        return self.__slots

    @property
    def efects(self):
        return self.__efects

    @efects.setter
    def efects(self, efects: list):
        self.__efects = efects

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, alive: bool):
        self.__alive = alive

    def castSpell(self, n_slot: int):
        now = time.time()
        if self.delay[n_slot] < now:
            print("slots", self.slots)
            print("magias", self.spell_list)
            self.slots[n_slot].cast(self)
            spell_casted = self.slots[n_slot]
            new_spell = random.choice(self.spell_list)
            self.slots[n_slot] = new_spell
            self.spell_list.remove(new_spell)
            self.spell_list.append(spell_casted)
            self.delay[n_slot] = time.time() + self.__cooldown
            print("pós slots", self.slots)
            print("pós magias", self.spell_list)

    def accelerate(self):
        self.__impulse = True

    def rotate(self, clockwise: bool):
        self.__rotating = True
        self.__clockwise = clockwise

    def update(self, dt):
        if self.__rotating:
            if self.__clockwise:
                self.ang -= self.__vel_ang
            else:
                self.ang += self.__vel_ang
            self.__rotating = False

        if self.__impulse:  # mover para frente se ha impulso
            new_vel = (self.vel[0] + self.angle_vector[0] * self.__accel,
                       self.vel[1] + self.angle_vector[1] * self.__accel)
            self.__impulse = False
        else:
            new_vel = self.vel

        # perda de velocidade por atrito:
        self.vel = (new_vel[0]*self.__atr, new_vel[1]*self.__atr)

        for effect in self.__effects:
            effect(self)

        super().update(dt)

    def add_effect(self, effect):
        self.__effects.append(effect)

    def effect_remove(self, effect):
        self.__effects.remove(effect)

    def damage(self, damage):
        if self.protection() in self.__effects:
            pass
        else:
            self.life -= damage
