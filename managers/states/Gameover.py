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

from managers import Game


class Gameover(State):
    def __init__(self, game: Game, state_name):
        super().__init__(game, state_name)
        temp_image = self.image.copy()

        self.__sel = 1
        self.__myfont = pg.font.Font(
            'fonts/EquipmentPro.ttf', 30)
        self.__raw_images = []

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
            self.__raw_images.append(temp_image.copy())

            pg.draw.rect(
                self.__raw_images[-1],
                (200, 50, 50),
                pg.Rect(pos, text.get_size()),
                width=3,
            )

    def redefine(self):
        return super().redefine()

    def Start(self, deaths):
        self.__scores = list(reversed(deaths))
        self.__menu_images = [i.copy() for i in self.__raw_images]
        screen_size_x = self.canvas.get_size()[0]
        pg.font.init()
        myfont = pg.font.SysFont('Comic Sans MS', 30)
        for x in range(len(self.__scores)):
            self.__scores[x].ang = 0
            imagem = self.__scores[x].image
            if x == 0:
                Text_image = myfont.render('winner', False, (255, 255, 0))
                hat_brigth_color = self.__scores[0].front_color
                hat_darker_color = self.__scores[0].color

            else:
                Text_image = myfont.render('loser', False, (0, 0, 0))

            for screen in self.__menu_images:
                var = pg.PixelArray(screen)
                var.replace((255, 127, 39), hat_brigth_color)
                var.replace((185, 122, 87), hat_darker_color)
                del var
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
                        return self.game.states_enum.Exit
                    elif self.__sel == 1:
                        return self.game.states_enum.Match
                    elif self.__sel == 2:
                        return self.game.states_enum.Menu

        self.canvas.blit(self.__menu_images[self.__sel], (0, 0))
