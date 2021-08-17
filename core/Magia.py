#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto

    Classe base para as magias
"""
from abc import ABC, abstractmethod
from core.Actor import Actor
from core.Mago import Mago


class Magia(ABC, Actor):
    def __init__(self, nome: str, icone: str, som: str,
                radius: float, image_dict: dict, size: tuple,
                ang: float, vel=(0, 0), groups=None):
        super(Magia, self).__init__(radius, image_dict, size, ang, vel, groups)
        self.__nome = nome
        self.__icone = icone
        self.__som = som
        

    @property
    def nome(self):
        return self.__nome

    @property
    def icone(self):
        return self.__icone

    @property
    def som(self):
        return self.__som

    @property
    def mago(self):
        return self.__mago

    @property
    def actor(self):
        return self.__actor

    @abstractmethod
    def cast(self, mago): 
        rect = mago.rect.center
        x =rect[0] - self.size[0]/2 
        y =rect[1] - self.size[1]/2
        self.rect.update(x, y, *self.size)
        self.revive()

    @abstractmethod
    def colisao(self):
        pass
