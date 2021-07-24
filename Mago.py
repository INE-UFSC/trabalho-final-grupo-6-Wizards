#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:02:51 2021

@author: 
    Guilherme Barcellos Neves
    Lucas Yuki Imamura
    Vitor Hugo Homem Marzarotto
"""
from Actor import Actor

class Mago(Actor):
    def __init__(self, id: int, vida_max: int, lista_magias: list, dano_base: int, accel: float,grupo,Image_dict:dict):
        self.__id = id
        self.__vida_max = vida_max
        self.__lista_magias = lista_magias
        self.__dano_base = dano_base
        self.__accel = accel
        self.__vida = vida_max
        self.__slots = [None, None, None]
        self.__efeitos = {}
        self.__vivo = True
        super().__init__(40,Image_dict,(0,0),1,(1,0),grupo)
    
 


    @property
    def id(self):
        return self.__id

    @property
    def vida_max(self):
        return self.__vida_max

    @property
    def lista_magias(self):
        return self.__lista_magias

    @property
    def dano_base(self):
        return self.__dano_base

    @property
    def accel(self):
        return self.__accel

    @property
    def vida(self):
        return self.__vida

    @property
    def slots(self):
        return self.__slots
    
    @property
    def efeitos(self):
        return self.__efeitos

    @property
    def vivo(self):
        return self.__vivo

    @vida.setter
    def vida(self, vida: int):
        self.__vida = vida
    
    @efeitos.setter
    def efeitos(self, efeitos: dict):
        self.__efeitos = efeitos
    
    @vivo.setter
    def vivo(self, vivo: bool):
        self.__vivo = vivo


    def jogarMagia(self, n_slot: int):
        pass

    def acelerar(self):
        self.vel = (2,0)

    def rotacionar(self, sentido_horario: bool):
        pass