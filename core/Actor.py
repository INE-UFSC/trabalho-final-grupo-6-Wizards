#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from pygame.sprite import Sprite
from pygame import Rect


class Actor(Sprite):
    def __init__(self, radius: float, image_dict: dict, size: tuple,
                 framerate: float, ang: int, vel=(0, 0), groups=None):
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

        self.radius = radius
        self.__image_dict = image_dict
        self.__size = size
        self.__framerate = framerate
        self.__vel = vel
        self.ang = ang
        super().__init__(groups)

        self.__rect = Rect(0, 0, *size)
        self.image = self.__image_dict[list(self.__image_dict.keys())[0]]

    @property
    def rect(self):
        return self.__rect

    @property
    def vel(self):
        return self.__vel

    @vel.setter
    def vel(self, vel):
        self.__vel = vel

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
        self.rect.move_ip(*self.vel)
