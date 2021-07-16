#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:02:51 2021

@author: 
    Guilherme Barcellos Neves
    Lucas Yuki Imamura
    Vitor Hugo Homem Marzarotto
"""
from abc import ABC, abstractmethod
from Actor import Actor
from Mago import Mago

class Magia(ABC):
    def __init__(self, nome: str, icone: str, som: str, mago: Mago, actor: Actor):
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