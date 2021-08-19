#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto

    Manages the match
"""
import pygame as pg
from pygame.sprite import groupcollide
# import time
# from pygame.constants import K_0

from managers import Inputs
from managers.states import State
from core import Wizard, RSurface
from core.spells import Curse, Bullet, Shield, Fireball

from core.MathFuncions import circle_colide


class Match(State):
    def Redefinir(self):
        self.__wizard_group = pg.sprite.Group()
        self.__spell_group = pg.sprite.Group()

    def Start(self, n_players: int = 1):
        self.Redefinir()

        self.__n_players = n_players

        R = 25
        width = 3
        self.__wizards = []
        for p in range(n_players):
            Mage_image = RSurface(R, (R*2, R*2), pg.SRCALPHA)
            pg.draw.circle(Mage_image, (255, 0, 0), (R, R), R)
            pg.draw.rect(Mage_image, (0, 255, 0),
                         pg.Rect(R, R-width/2, R, width))

            W_image_dict = {'temp': Mage_image}
            W_sound_dict = {'temp': "wizard_sound"}

            spell_list = [Curse(p, [self.__spell_group]),
                          Bullet(p, [self.__spell_group]),
                          Shield(p, [self.__spell_group]),
                          Fireball(p, [self.__spell_group])]

            wizard = Wizard(idx=p, max_life=10, spell_list=spell_list,
                            base_damage=2, ang=0, groups=[self.__wizard_group],
                            Image_dict=W_image_dict, sound_dict=W_sound_dict,
                            accel=0.25, atr=0.99)

            self.__wizards.append(wizard)

        self.__inputs = Inputs(*self.config.p[: n_players])

    def __process___inputs(self):
        actions = self.__inputs.get()
        for p in range(self.__n_players):
            if 0 in actions[p]:  # turn_r
                if 1 not in actions[p]:  # not turn_l
                    self.__wizards[p].rotate(True)
            elif 1 in actions[p]:  # turn_l
                self.__wizards[p].rotate(False)

            if 2 in actions[p]:  # acc
                if 3 not in actions[p]:  # dacc
                    self.__wizards[p].accelerate()
            elif 3 in actions[p]:  # dacc
                pass  # desacelerar

            if 4 in actions[p]:  # slot0
                self.__wizards[p].castSpell(0)
            if 5 in actions[p]:  # slot1
                self.__wizards[p].castSpell(1)
            if 6 in actions[p]:  # slot2
                self.__wizards[p].castSpell(2)

    def run(self):
        colided = groupcollide(self.__wizard_group, self.__spell_group,
                               False, False, circle_colide)
        for wizard, spells in colided.items():
            for spell in spells:
                spell.colision(wizard)

        self.__process___inputs()

        self.canvas.fill((0, 200, 200))

        self.__spell_group.draw(self.canvas)
        self.__spell_group.update(1)
        self.__wizard_group.draw(self.canvas)
        self.__wizard_group.update(1)

        return 1
