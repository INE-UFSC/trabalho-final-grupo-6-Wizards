#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg

from managers.UI import UIabstract


class UIcorner(UIabstract):
    __x_offset = 30
    __y_offset = 70
    __bar_x = 300
    __bar_y = 10
    __icon_offset = 10

    def redefine(self):
        super().redefine()
        self.__bar_pos = [
            (self.__x_offset,
             self.__y_offset),
            (self.screen_size[0]-self.__x_offset-self.__bar_x,
             self.__y_offset),
            (self.__x_offset,
             self.screen_size[1]-self.__y_offset-self.__bar_y),
            (self.screen_size[0]-self.__x_offset-self.__bar_x,
             self.screen_size[1]-self.__y_offset-self.__bar_y)
            ]
        self.__icon_pos = [
            (self.__icon_offset,
             self.__icon_offset),
            (self.screen_size[0]-(self.__icon_offset + self.icon_size[0]) * 3,
             self.__icon_offset),
            (self.__icon_offset,
             self.screen_size[1]-self.__icon_offset-self.icon_size[1]),
            (self.screen_size[0]-(self.__icon_offset + self.icon_size[0]) * 3,
             self.screen_size[1]-self.__icon_offset-self.icon_size[1])
            ]

    def __hp_bar(self, canvas):
        for i in range(self.n_wiz):
            wiz = self.wizards[i]
            percentage = int(self.__bar_x * wiz.life / wiz.max_life)

            bar = pg.Surface((self.__bar_x, self.__bar_y))
            bar.fill((255, 0, 0))
            pg.draw.rect(bar, (0, 255, 50), pg.Rect(0, 0, percentage, 10))
            canvas.blit(bar, self.__bar_pos[i])

    def __spell_icons(self, canvas):
        for i in range(self.n_wiz):
            slots = self.wizards[i].slots
            x = self.__icon_pos[i][0]
            y = self.__icon_pos[i][1]
            for s in range(3):
                canvas.blit(slots[s].icon, (x, y))
                x += self.icon_size[0] + self.__icon_offset

    def draw(self, canvas, time: int):
        super().draw(canvas, time)
        self.__hp_bar(canvas)
        self.__spell_icons(canvas)
