#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto

    Classe base para gerenciadores (estados do jogo).
"""
from abc import ABC, abstractmethod
import pygame as pg
import os
from managers import Game


class State(ABC):
    def __init__(self, game: Game, state_name):
        self.__game: Game = game
        self.__image = pg.image.load(
            os.path.join('images', state_name+'_img.png'))
        self.__image = pg.transform.scale(self.__image, self.window.get_size())
        self.__canvas: pg.surface.Surface = pg.Surface(self.window.get_size())
        self.__canvas.blit(self.__image, (0, 0))
        self.redefine()

    @property
    def image(self):
        return self.__image

    @property
    def game(self):
        return self.__game

    @property
    def window(self):
        return self.__game.window

    @property
    def canvas(self):
        return self.__canvas

    @property
    def config(self):
        return self.game.config

    @abstractmethod
    def redefine(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def display(self):
        self.window.blit(self.canvas, (0, 0))
        pg.display.update()
