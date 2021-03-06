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

from pygame.constants import CONTROLLER_AXIS_INVALID

from managers.states import State
from managers.Config import Config

from managers import Game


class Menu(State):
    def __init__(self, game: Game, state_name):
        super().__init__(game, state_name)
        self.__states = 3

        self.__myfont = pg.font.Font(
            'fonts/EquipmentPro.ttf', 100)

        canvas_size = self.canvas.get_size()

        title_img = pg.image.load(
            os.path.join('images', 'title_img.png'))
        title_img = pg.transform.scale(
            title_img, (int(canvas_size[0] * 0.9), int(canvas_size[0] * 0.087)))
        x = (canvas_size[0] - title_img.get_size()[0]) / 2
        y = canvas_size[1] * 0.01
        self.image.blit(title_img, (x, y))

        button_text = [("Play", 0.3), ("Settings", 0.5), ("Quit", 0.7)]
        for i in range(len(button_text)):
            text, pos = button_text[i]
            textsurface = self.__myfont.render(text, False, (0, 0, 0))
            x = (canvas_size[0] - textsurface.get_size()[0]) / 2
            y = canvas_size[1] * pos
            self.image.blit(textsurface, (x, y))
            button_text[i] = (textsurface, (x, y))
        self.__button_play = (button_text[0][1][0] + 110, button_text[0][1][1])
        textsurface = self.__myfont.render("N° players", False, (0, 0, 0))
        self.__n_players_size = textsurface.get_size()
        self.image.blit(
            textsurface,
            (self.__button_play[0] + 40, self.__button_play[1] - 70)
        )

        self.__menu_images = []
        for text, pos in button_text:
            self.__menu_images.append(self.image.copy())

            pg.draw.rect(
                self.__menu_images[-1],
                (200, 50, 50),
                pg.Rect(pos, text.get_size()),
                width=3,
            )

    @ property
    def players(self):
        return self.__players

    def redefine(self):
        self.__sel = 0
        self.__players = 2

    def Start(self):
        self.redefine()
        pg.mixer.music.load(
            os.path.join('sounds', 'states', "menu_sound.wav"))
        pg.mixer.music.set_volume(0.15)
        pg.mixer.music.play(-1)

    def run(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return self.game.states_enum.Exit

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.__sel = (self.__sel - 1) % self.__states

                if event.key == pg.K_DOWN:
                    self.__sel = (self.__sel + 1) % self.__states

                if event.key == pg.K_RETURN:
                    if self.__sel == 0:
                        return self.game.states_enum.Match
                    elif self.__sel == 1:
                        return self.game.states_enum.Options
                    elif self.__sel == 2:
                        return self.game.states_enum.Exit

                if event.key == pg.K_LEFT:
                    if self.__sel == 0:
                        if self.__players == 2:
                            self.__players = 4
                        else:
                            self.__players -= 1

                if event.key == pg.K_RIGHT:
                    if self.__sel == 0:
                        if self.__players == 4:
                            self.__players = 2
                        else:
                            self.__players += 1

        self.canvas.blit(self.__menu_images[self.__sel].copy(), (0, 0))
        textsurface = self.__myfont.render(
            str(self.__players), False, (0, 0, 0))
        self.canvas.blit(
            textsurface, (self.__button_play[0] + 40 + self.__n_players_size[0]/2, self.__button_play[1] + 30))

        return None  # continua no menu
