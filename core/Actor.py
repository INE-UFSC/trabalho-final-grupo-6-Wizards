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


class Actor(Sprite):
    def __init__(self, radius: float, image_dict: dict, size: tuple,
                 ang: float, vel=(0, 0), groups=None):
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

        self.__radius = radius
        self.__radius2 = radius*radius
        self.__image_dict = image_dict
        self.__size = size
        self.vel = vel
        self.__rect = pg.Rect(0, 0, *size)
        self.ang = ang
        self.__change_ang = True
        self.state = list(self.__image_dict.keys())[0]
        super().__init__(groups)

        self.__new_angle = True
        self.__moving = True
        self.__image = self.__image_dict[self.state]
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
    def size(self):
        return self.__size

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
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image
    
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
                         *self.__image.get_size() )
        
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
        if self.__new_angle:
            self.__rotate()
