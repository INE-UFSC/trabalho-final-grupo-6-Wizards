#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from abc import ABC, abstractmethod
import pygame as pg

from core import Wizard


class UIabstract(ABC):
    def __init__(self, wizards: list[Wizard], screen_size):
        self.__wizards = wizards
        self.__n_wiz = len(wizards)
        self.__screen_size = screen_size
        self.__group = pg.sprite.Group()
        self.__myfont = pg.font.SysFont('Comic Sans MS', 30)
        
        self.__icon_size = wizards[0].slots[0].icon.get_size()

        self.redefine()

    def redefine(self):
        self.__player_id = []
        self.__player_id_size = []
        for i in range(self.__n_wiz):
            self.__player_id.append(self.__myfont.render(
                "P%i" % (i+1), False, self.__wizards[i].color))
            self.__player_id_size.append(self.__player_id[-1].get_size())

    @property
    def wizards(self):
        return self.__wizards

    @property
    def n_wiz(self):
        return self.__n_wiz

    @property
    def screen_size(self):
        return self.__screen_size

    @property
    def group(self):
        return self.__group

    @property
    def my_font(self):
        return self.__my_font

    @property
    def icon_size(self):
        return self.__icon_size

    def __draw_player_identifier(self, canvas):
        for i in range(self.__n_wiz):
            wizard = self.__wizards[i]
            size = self.__player_id_size[i]
            x = wizard.rect.center[0] - size[0] / 2
            y = wizard.rect.center[1] - 50 - size[1] / 2
            canvas.blit(self.__player_id[i], (x, y))

    def draw(self, canvas, time: int):
        self.__draw_player_identifier(canvas)
