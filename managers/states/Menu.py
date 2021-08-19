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

from managers.states import State
from managers.Config import Config


class Menu(State):
    def __init__(self, window: pg.surface.Surface, config: Config):
        super().__init__(window, config)
        self.__states = 3
        #def images(i): return os.path.join('images', 'menu_'+str(i)+'.png')
        #self.__menu_images = [pg.image.load(images(i)) for i in range(3)]
        myfont = pg.font.SysFont('Comic Sans MS', 30)

        temp_image = self.canvas.copy()
        temp_image.fill((50, 250, 50))
        canvas_size = self.canvas.get_size()
        button_text = [('Play', 0.3), ('Config', 0.5), ('Quit', 0.7)]
        for i in range(len(button_text)):
            text, pos = button_text[i]
            textsurface = myfont.render(text, False, (0, 0, 0))
            x = (canvas_size[0]-textsurface.get_size()[0])/2
            y = canvas_size[1]*pos
            temp_image.blit(textsurface, (x, y))
            button_text[i] = (textsurface, (x, y))

        self.__menu_images = []
        for text, pos in button_text:
            self.__menu_images.append(temp_image.copy())

            pg.draw.rect(
                self.__menu_images[-1], (200, 50, 50),
                pg.Rect(pos, text.get_size()), width=3)

    def Redefinir(self):
        self.__sel = 0

    def run(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.__sel = (self.__sel-1) % self.__states

                if event.key == pg.K_DOWN:
                    self.__sel = (self.__sel+1) % self.__states

                if event.key == pg.K_RETURN:
                    if self.__sel == 0:
                        return 1  # play
                    elif self.__sel == 1:
                        return 2  # config
                    elif self.__sel == 2:
                        return -1  # quit

        self.canvas.blit(self.__menu_images[self.__sel], (0, 0))
        return 0  # continua no menu
