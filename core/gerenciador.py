#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import time
import pygame as pg
from core.Mago import Mago
from pygame.constants import K_0

import os


class Gerenciador():

    def __init__(self, canvas, window):
        self.canvas = canvas
        self.window = window
        images = lambda i: os.path.join('images', 'menu_'+str(i)+'.png')
        self.menu_images = [pg.image.load(images(i)) for i in range(3)]

        self.Redefinir()

        self.testVar = 0

    def Redefinir(self):
        self.M_grupo = pg.sprite.Group()

        Mage_image = pg.Surface((80, 80), pg.SRCALPHA)
        pg.draw.circle(Mage_image, (255, 0, 0), (40, 40), 40)
        M_image_dict = {'bola': Mage_image}

        self.MagoTest = Mago(0, 0, [], 2, 1, self.M_grupo, M_image_dict)

    def partida(self):
        FPS = 60
        clock = pg.time.Clock()
        prev_time = time.time()
        dt = 0

        running = True
        while running:

            clock.tick(FPS)

            now = time.time()
            dt = (now - prev_time)*60
            prev_time = now

            for event in pg.event.get():

                if event.type == pg.QUIT:

                    running = False

            keys = pg.key.get_pressed()
            if keys[K_0]:
                self.MagoTest.acelerar()

            self.canvas.fill((0, 200, 200))

            self.MagoTest.update(self.canvas, dt, (0, 0))
            self.M_grupo.draw(self.canvas)

            self.window.blit(self.canvas, (0, 0))
            pg.display.update()
