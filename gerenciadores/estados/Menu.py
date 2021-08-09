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

from gerenciadores.estados.Estado import Estado
from gerenciadores.Config import Config


class Menu(Estado):
    def __init__(self, window: pg.surface.Surface, config: Config):
        super().__init__(window, config)
        images = lambda i: os.path.join('images', 'menu_'+str(i)+'.png')
        self.__menu_images = [pg.image.load(images(i)) for i in range(3)]

    def Redefinir(self):
        self.__sel = 0

    def run(self):
        self.__sel += 1
        if self.__sel > 2:
            self.__sel = 0
        self.canvas.blit(self.__menu_images[self.__sel], (0, 0))
        return 1
