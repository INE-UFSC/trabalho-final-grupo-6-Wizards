#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg
from pygame import gfxdraw
from core import GameObject, RSurface
from images import circle
import os
import random
import time


class Wizard(GameObject):
    __colors = [(200, 20, 20), (50, 50, 255), (20, 150, 20), (200, 200, 50)]

    def __init__(
        self,
        idx: int,
        max_life: int,
        spell_list: list,
        base_damage: int,
        ang: float,
        screen_size: tuple,
        groups: list,
        acc_ang=5,
        accel=0.5,
        atr=0.99,
    ):
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
        self.__color = self.__colors[idx]
        self.shield = None

        R = 25
        width = 4

        Mage_image = RSurface(R, (R * 2+2, R * 2+2), pg.SRCALPHA)
        circle(R, self.__color, surface=Mage_image, pos=(R, R))

        # imagem = pg.image.load(os.path.join(
        #    'images', 'mago_teste.png')).convert()
        #imagem = pg.transform.scale(imagem, (R*2, R*2))
        #Mage_image.blit(imagem, (0, 0))

        # draw_circle(Mage_image, R, R, R, self.__color)
        # gfxdraw.box(Mage_image, pg.Rect(R, R - width / 2, R, width), (0, 0, 0))
        # pg.draw.circle(Mage_image, self.__color, (R, R), R)
        # pg.draw.rect(Mage_image, (0, 0, 0), pg.Rect(R, R - width / 2, R, width))

        image_dict = {"1": {"path": os.path.join(
            'images', 'mago_teste.png'), "R": R, "size": (
            R*2+2, R*2+2)}}
        sound_dict = {"temp": "wizard_sound"}
        self.__damageSound = pg.mixer.Sound(os.path.join(
            'Sounds', sound_dict["temp"]+".wav"))
        self.__shieldSound = pg.mixer.Sound(
            os.path.join('Sounds', 'spells', "shield_sound.wav"))
        super().__init__(
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=ang,
            screen_size=screen_size,
            vel=(0, 0),
            groups=groups,
        )
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

        self.delay = [3, 3, 3]

    @ property
    def idx(self):
        return self.__idx

    @ property
    def max_life(self):
        return self.__max_life

    @ property
    def spell_list(self):
        return self.__spell_list

    @ property
    def base_damage(self):
        return self.__base_damage

    @ property
    def accel(self):
        return self.__accel

    @ property
    def life(self):
        return self.__life

    @ life.setter
    def life(self, life: int):
        self.__life = life

    @ property
    def slots(self):
        return self.__slots

    @ property
    def efects(self):
        return self.__efects

    @ property
    def alive(self):
        return self.__alive

    @ alive.setter
    def alive(self, alive: bool):
        self.__alive = alive

    @ property
    def color(self):
        return self.__color

    def castSpell(self, n_slot: int):
        now = time.time()
        if self.delay[n_slot] < now:
            self.slots[n_slot].cast(self)
            spell_casted = self.slots[n_slot]
            new_spell = random.choice(self.spell_list)
            self.slots[n_slot] = new_spell
            self.spell_list.remove(new_spell)
            self.spell_list.append(spell_casted)
            self.delay[n_slot] = time.time() + self.__cooldown
            # print("slots",self.slots)
            # print(self.spell_list)

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
            new_vel = (
                self.vel[0] + self.angle_vector[0] * self.__accel,
                self.vel[1] + self.angle_vector[1] * self.__accel,
            )
            self.__impulse = False
        else:
            new_vel = self.vel

        # perda de velocidade por atrito:
        self.vel = (new_vel[0] * self.__atr, new_vel[1] * self.__atr)

        for effect in self.__effects:
            effect(self)

        super().update(dt)

    def add_effect(self, effect):
        self.__effects.append(effect)

    def effect_remove(self, effect):
        self.__effects.remove(effect)

    def damage(self, damage):
        if self.shield is not None:
            self.__life -= self.shield.block(damage)
            self.__shieldSound.play()
        else:
            self.__damageSound.play()
            self.__life -= damage

        if self.__life <= 0:
            self.kill()
            self.alive = False
