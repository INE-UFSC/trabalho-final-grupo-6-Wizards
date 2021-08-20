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


class GameObject(Sprite):
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
    def image(self):
        return self.__image

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        self.__state = new_state
        old_center = self.__image.get_rect().center
        self.__image = self.__image_dict[self.__state]
        new_center = self.__image.get_rect().center

        img_size = self.__image.get_size()
        self.rect.update(self.rect[0]+old_center[0]-new_center[0],
                         self.rect[1]+old_center[1]-new_center[1],
                         *img_size)
        self.radius = self.__image.radius

        self.__lim_x_inf = self.__radius - img_size[0]/2
        self.__lim_y_inf = self.__radius - img_size[1]/2
        self.__lim_x_sup = self.__screen_size[0] - self.__radius - img_size[0]/2
        self.__lim_y_sup = self.__screen_size[1] - self.__radius - img_size[0]/2

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

    def __rotate(self):
        old_center = self.__image.get_rect().center
        self.__image = pg.transform.rotate(self.__image_dict[self.state],
                                           self.ang)
        new_center = self.__image.get_rect().center

        self.rect.update(self.rect[0]+old_center[0]-new_center[0],
                         self.rect[1]+old_center[1]-new_center[1],
                         *self.__image.get_size())

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
            self.rect.move_ip(*self.vel)
            #  melhorar dps espelhando o excesso
            if self.rect.x < self.lim_x_inf:
                self.rect.x = self.lim_y_inf
                self.vel = (-self.vel[0], self.vel[1])
            elif self.rect.x > self.lim_x_sup:
                self.rect.x = self.lim_x_sup
                self.vel = (-self.vel[0], self.vel[1])

            #  melhorar dps espelhando o excesso
            if self.rect.y < self.lim_y_inf:
                self.rect.y = self.lim_y_inf
                self.vel = (self.vel[0], -self.vel[1])
            elif self.rect.y > self.lim_y_sup:
                self.rect.y = self.lim_y_sup
                self.vel = (self.vel[0], -self.vel[1])

        if self.__new_angle:
            self.__rotate()
