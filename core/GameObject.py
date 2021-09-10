#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from pygame.sprite import Sprite
import pygame as pg
import math
import os


class GameObject(Sprite):
    __bounce_dist = 30

    def __init__(self, image_dict: dict, sound_dict: dict, ang: float,
                 screen_size: tuple, vel=(0, 0), groups=None):
        """
        Parameters
        ----------
        radius : float
            Raio do Ator (para bounding box).
        image_dict : dict
            Dicionario com os sprites do Ator.
        size : tuple
            Tamanho do Ator.
        framerate : float
            Quantidade de frames por segundo
        vel : TYPE, optional
            Velocidade inicial. The default is (0, 0).
        groups : TYPE, optional
            Grupo inicial. The default is None.
        """
        self.__rect = pg.Rect(0, 0, 0, 0)
        self.__center = [0, 0]

        self.__image_dict = image_dict
        self.vel = vel
        self.ang = ang
        self.__change_ang = True
        self.__screen_size = screen_size

        self.__state = list(self.__image_dict.keys())[0]
        self.__image = self.__image_dict[self.__state]

        self.state = self.__state

        super().__init__(groups)

        self.__new_angle = True
        self.__moving = True
        self.__savedgroup = groups

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius
        self.__radius2 = radius*radius

    @property
    def radius2(self):
        return self.__radius2

    @property
    def vel(self):
        return self.__vel

    @vel.setter
    def vel(self, vel):
        self.__vel = vel
        if abs(self.__vel[0]) + abs(self.__vel[1]) > 0:
            self.__moving = True
        else:
            self.__moving = False

    @property
    def ang(self):
        return self.__ang

    @ang.setter
    def ang(self, ang):
        self.__ang = ang
        self.__new_angle = True
        self.calc_angle_vector()

    @property
    def angle_vector(self):
        return self.__angle_vector

    def calc_angle_vector(self):
        ang = math.radians(self.ang)
        self.__angle_vector = (math.cos(ang), -math.sin(ang))

    @property
    def screen_size(self):
        return self.__screen_size

    @property
    def rect(self):
        return self.__rect

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, pos: list):
        try:
            pos = list(pos)
            assert len(pos) == 2
        except (TypeError, AssertionError) as e:
            print("'pos' must be an iterable with x in the first" +
                  "position and y in the second")
            raise e

        self.__center = pos
        self.__centralize_image()

    @property
    def image(self):
        return self.__image

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        self.__state = new_state
        self.__image = self.__image_dict[self.__state]

        self.__centralize_image()
        self.radius = self.__image.radius

        self.__lim_x_inf = self.__radius + self.__bounce_dist
        self.__lim_y_inf = self.__radius + self.__bounce_dist
        temp = self.__radius + self.__bounce_dist
        self.__lim_x_sup = self.__screen_size[0] - temp
        self.__lim_y_sup = self.__screen_size[1] - temp

    @property
    def lim_x_inf(self):
        return self.__lim_x_inf

    @property
    def lim_y_inf(self):
        return self.__lim_y_inf

    @property
    def lim_x_sup(self):
        return self.__lim_x_sup

    @property
    def lim_y_sup(self):
        return self.__lim_y_sup

    def revive(self):
        for g in self.__savedgroup:
            g.add(self)

    def __centralize_image(self):
        img_size = self.__image.get_size()
        h_size = (img_size[0]/2, img_size[1]/2,)
        self.__rect.update(self.__center[0]-h_size[0],
                           self.__center[1]-h_size[1],
                           *img_size)

    def __rotate(self):
        self.__image = pg.transform.rotate(self.__image_dict[self.state],
                                           self.ang)
        self.__centralize_image()

    def move(self, x, y):
        self.__center[0] += x
        self.__center[1] += y

        #  melhorar dps espelhando o excesso
        if self.__center[0] < self.lim_x_inf:
            self.__center[0] = self.lim_x_inf
            self.vel = (-self.vel[0], self.vel[1])
        elif self.__center[0] > self.lim_x_sup:
            self.__center[0] = self.lim_x_sup
            self.vel = (-self.vel[0], self.vel[1])

        #  melhorar dps espelhando o excesso
        if self.__center[1] < self.lim_y_inf:
            self.__center[1] = self.lim_y_inf
            self.vel = (self.vel[0], -self.vel[1])
        elif self.__center[1] > self.lim_y_sup:
            self.__center[1] = self.lim_y_sup
            self.vel = (self.vel[0], -self.vel[1])

        self.__centralize_image()

    def update(self, dt):
        """
        Parameters
        ----------
        new_pos : TYPE, optional
            Forçar nova posição do autor, se nada for passado, é calculado
                com base na posição antiga e velocidade atual.
                The default is None.

        Returns
        -------
        new_pos: tuple
            Nova posição do Ator.

        """
        if self.__moving:
            self.move(*self.vel)

        if self.__new_angle:
            self.__rotate()
