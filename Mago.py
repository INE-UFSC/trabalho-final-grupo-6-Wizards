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
import math

class Mago(Actor):
    def __init__(self, id: int, vida_max: int, lista_magias: list, 
    dano_base: int, ang: int, impulse: bool, grupo,Image_dict:dict, vel_ang: 0, accel: 0.5):
        self.__id = id
        self.__vida_max = vida_max
        self.__lista_magias = lista_magias
        self.__dano_base = dano_base
        self.__accel = accel
        self.__vida = vida_max
        self.__slots = [None, None, None]
        self.__efeitos = {}
        self.__vivo = True
        self.impulse = impulse
        super().__init__(40,Image_dict,(0,0),1,ang,(1,0),grupo)
        self.vel_ang = vel_ang
    
 


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

    def angle_vector(ang):
        return (math.cos(ang), -math.sin(ang))

    def update(self):
        atr = self.__accel / 20

        self.ang += self.vel_ang ##deslocamento angular
        
        if self.impulse: ## mover para frente se ha impulso
            self.forward = self.angle_vector(math.radians(self.ang))
            self.vel[0] += self.forward[0] * self.__accel
            self.vel[1] += self.forward[1] * self.__accel

        ##perda de velocidade por atrito: 
        self.vel[0] *= (1 - atr)
        self.vel[1] *= (1 - atr)

        super().update()

    
        
        


