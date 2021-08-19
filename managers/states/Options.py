#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg

from managers.states import State
from managers.Config import Config


class Options(State):
    def __init__(self, window: pg.surface.Surface, config: Config):
        super().__init__(window, config)

    def run(self):
        pass

    def Redefinir(self):
        pass
