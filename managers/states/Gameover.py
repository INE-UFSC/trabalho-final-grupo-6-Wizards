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
