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

from gerenciadores.Config import Config


class Estado(ABC):
    def __init__(self, window: pg.surface.Surface, config: Config):
        self.__window: pg.surface.Surface = window
        self.__canvas: pg.surface.Surface = pg.Surface(window.get_size())
        self.__config: Config = config
        self.Redefinir()

    @property
    def window(self):
        return self.__window

    @property
    def canvas(self):
        return self.__canvas

    @property
    def config(self):
        return self.__config

    @abstractmethod
    def Redefinir(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def display(self):
        self.window.blit(self.canvas, (0, 0))
        pg.display.update()
