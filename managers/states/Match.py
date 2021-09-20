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
from core.spells import Curse, Bullet, Shield, Fireball, Teleport, Wind

from core.MathFuncions import circle_colide
import time


class Match(State):
    __init_pos = [lambda size: (size[0]*0.1, size[1]*0.2),
                  lambda size: (size[0]*0.9, size[1]*0.2),
                  lambda size: (size[0]*0.1, size[1]*0.8),
                  lambda size: (size[0]*0.9, size[1]*0.8)]

    def redefine(self):
        self.__init_time = time.time()
        self.__wizard_group = pg.sprite.Group()
        self.__spell_group = pg.sprite.Group()

    def Start(self, n_players: int = 1):
        self.redefine()

        screen_size = self.canvas.get_size()

        self.__n_players = n_players
        self.__deaths = []  # lista de magos que morreram

        self.__wizards = []
        for p in range(n_players):
            spell_list = [
                Wind(p, [self.__spell_group], screen_size),
                Teleport(p, [self.__spell_group], screen_size),
                Curse(p, [self.__spell_group], screen_size),
                Bullet(p, [self.__spell_group], screen_size),
                Shield(p, [self.__spell_group], screen_size),
                Fireball(p, [self.__spell_group], screen_size)
            ]

            wizard = Wizard(
                idx=p,
                max_life=10,
                spell_list=spell_list,
                base_damage=2,
                ang=0,
                screen_size=screen_size,
                groups=[self.__wizard_group],
                accel=0.25,
                atr=0.99,
            )

            wizard.center = self.__init_pos[p](screen_size)
            self.__wizards.append(wizard)

        self.__inputs = Inputs(*self.config.p[:n_players])
        self.__UI = UIcorner(self.__wizards, screen_size, self.canvas)

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
        time_now = time.time() - self.__init_time
        self.__now = 90 - int(time_now)
        if self.__now <= 0:
            self.__deaths += self.get_winner()
            return self.game.states_enum.Gameover

        self.__process___inputs()
        self.__colision_detect()

        self.__spell_group.update(1)
        self.__wizard_group.update(1)

        self.__draw()

        if self.verify_end():
            return self.game.states_enum.Gameover
        return None

    def __colision_detect(self):
        colided = groupcollide(self.__wizard_group, self.__spell_group,
                               False, False, circle_colide)
        for wizard, spells in colided.items():
            for spell in spells:
                spell.colision(wizard)

    def __draw(self):
        self.canvas.fill((250, 250, 250))
        self.__spell_group.draw(self.canvas)
        self.__wizard_group.draw(self.canvas)
        self.__UI.draw(time=self.__now)

    def verify_end(self):
        for wizard in self.__wizards:
            if wizard not in self.__deaths:
                if not wizard.alive:
                    self.__deaths.append(wizard)
                    if len(self.__deaths) == self.__n_players - 1:
                        self.__deaths += self.get_winner()
                        return True
        return False

    def get_winner(self):
        alive = []
        for wizard in self.__wizards:
            if wizard not in self.__deaths:
                alive.append(wizard)
        return alive

    @property
    def deaths(self):
        return self.__deaths
