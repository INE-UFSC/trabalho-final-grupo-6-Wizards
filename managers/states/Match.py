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
from managers.UI import UIcorner
from core import Wizard
from core.spells import Curse, Bullet, Shield, Fireball

from core.MathFuncions import circle_colide


class Match(State):
    __init_pos = [(0, 0), (200, 0), (0, 200), (200, 200)]

    def redefine(self):
        self.__wizard_group = pg.sprite.Group()
        self.__spell_group = pg.sprite.Group()

    def Start(self, n_players: int = 1):
        self.redefine()

        screen_size = self.canvas.get_size()

        self.__n_players = n_players

        self.__wizards = []
        for p in range(n_players):
            spell_list = [Curse(p, [self.__spell_group], screen_size),
                          Bullet(p, [self.__spell_group], screen_size),
                          Shield(p, [self.__spell_group], screen_size),
                          Fireball(p, [self.__spell_group], screen_size)]

            wizard = Wizard(idx=p, max_life=10, spell_list=spell_list,
                            base_damage=2, ang=0, screen_size=screen_size,
                            groups=[self.__wizard_group],  accel=0.25,
                            atr=0.99)

            wizard.rect.move_ip(*self.__init_pos[p])
            self.__wizards.append(wizard)

        self.__inputs = Inputs(*self.config.p[: n_players])
        self.__UI = UIcorner(self.__wizards, screen_size)

    def __process___inputs(self):
        actions = self.__inputs.get()
        for p in range(self.__n_players):
            if 0 in actions[p]:  # turn_r
                if 1 not in actions[p]:  # not turn_l
                    self.__wizards[p].rotate(True)
            elif 1 in actions[p]:  # turn_l
                self.__wizards[p].rotate(False)

            if 2 in actions[p]:  # acc
                self.__wizards[p].accelerate()

            if 3 in actions[p]:  # slot0
                self.__wizards[p].castSpell(0)
            if 4 in actions[p]:  # slot1
                self.__wizards[p].castSpell(1)
            if 5 in actions[p]:  # slot2
                self.__wizards[p].castSpell(2)

    def run(self):
        colided = groupcollide(self.__wizard_group, self.__spell_group,
                               False, False, circle_colide)
        for wizard, spells in colided.items():
            for spell in spells:
                spell.colision(wizard)

        self.__process___inputs()

        self.canvas.fill((250, 250, 250))

        self.__spell_group.update(1)
        self.__wizard_group.update(1)

        self.__spell_group.draw(self.canvas)
        self.__wizard_group.draw(self.canvas)
        self.__UI.draw(self.canvas, time=0)

        return None
