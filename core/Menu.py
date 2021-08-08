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


class Menu():
    def __init__(self, canvas, window):
        self.canvas = canvas
        self.window = window
        images = lambda i: os.path.join('images', 'menu_'+str(i)+'.png')
        self.menu_images = [pg.image.load(images(i)) for i in range(3)]

        self.testVar = 0

    def run(self):
        self.testVar += 1
        if self.testVar > 2:
            self.testVar = 0
        self.canvas.blit(self.menu_images[self.testVar], (0, 0))
        self.window.blit(self.canvas, (0, 0))
        pg.display.update()
