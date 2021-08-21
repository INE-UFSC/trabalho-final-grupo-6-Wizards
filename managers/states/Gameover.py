#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg
import os

from managers.states import *
from managers.Config import *


class Gameover(State):
    def __init__(self, window: pg.surface.Surface, config: Config):
        super().__init__(window, config)
        temp_image = self.canvas.copy()
        temp_image.fill((50, 250, 50))

        self.__sel = 1
        self.__myfont = pg.font.SysFont("Comic Sans MS", 30)
        self.__menu_images = []

        canvas_size = self.canvas.get_size()
        button_text = [("Exit Game", 0.3), ("Play Again", 0.5), ("Menu", 0.7)]
        for i in range(len(button_text)):
            text, pos = button_text[i]
            textsurface = self.__myfont.render(text, False, (0, 0, 0))
            x = canvas_size[0] * pos
            y = canvas_size[1]*0.8
            temp_image.blit(textsurface, (x, y))
            button_text[i] = (textsurface, (x, y))

        for text, pos in button_text:
            self.__menu_images.append(temp_image.copy())

            pg.draw.rect(
                self.__menu_images[-1],
                (200, 50, 50),
                pg.Rect(pos, text.get_size()),
                width=3,
            )

    def redefine(self):
        return super().redefine()

    def Start(self, deaths):
        self.__scores = list(reversed(deaths))
        screen_size_x = self.canvas.get_size()[0]
        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 30)
        for x in range(len(self.__scores)):
            self.__scores[x].ang = 0
            imagem = self.__scores[x].image
            if x == 0:
                Text_image = myfont.render('winner', False, (255, 255, 0))
            else:
                Text_image = myfont.render('loser', False, (0, 0, 0))

            for screen in self.__menu_images:
                screen.blit(
                    imagem, (screen_size_x/5*(x+1), 200))
                screen.blit(
                    Text_image, (screen_size_x/5*(x+1)-15, 100))

    def run(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.__sel = (self.__sel + 1) % 3

                if event.key == pg.K_LEFT:
                    self.__sel = (self.__sel - 1) % 3

                if event.key == pg.K_RETURN:
                    if self.__sel == 0:
                        return -1  # exit
                    elif self.__sel == 1:
                        return 1  # play
                    elif self.__sel == 2:
                        return 0  # menu

        self.canvas.blit(self.__menu_images[self.__sel], (0, 0))
