#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from abc import ABC, abstractmethod
from core.Actor import Actor
from core.Mago import Mago


class Magia(ABC):
    def __init__(self, nome: str, icone: str, som: str, mago: Mago,
                 actor: Actor):
        self.__nome = nome
        self.__icone = icone
        self.__som = som
        self.__mago = mago
        self.__actor = actor

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
    def lancarMagia(self):
        pass

    @abstractmethod
    def colisao(self):
        pass
