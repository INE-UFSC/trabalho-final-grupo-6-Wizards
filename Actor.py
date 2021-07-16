#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:02:51 2021

@author: 
    Guilherme Barcellos Neves
    Lucas Yuki Imamura
    Vitor Hugo Homem Marzarotto
"""
from pygame.sprite import Sprite
from pygame import Rect

class Actor(Sprite):
    def __init__(self, radius: float, image_dict: dict, size: tuple, framerate: float,
                 vel = (0, 0), groups = None):
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
            Quantidade de frames por segundo.
        vel : TYPE, optional
            Velocidade inicial. The default is (0, 0).
        groups : TYPE, optional
            Grupo inicial. The default is None.
        """
        self.__radius = radius
        self.__image_dict = image_dict
        self.__size = size
        self.__framerate = framerate
        self.__vel = vel
        super().__init__(groups)

        self.__rect = Rect(0, 0, *size)
        self.__image = self.__image_dict[list(self.__image_dict.values())[0]]

    def update(self, new_pos = None):
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
        if not new_pos:
            new_pos = (self.__rect.x + self.__vel[0]/self.__framerate,
                       self.__rect.y + self.__vel[1]/self.__framerate)
        self.__rect.move_ip(*new_pos)
        return new_pos
