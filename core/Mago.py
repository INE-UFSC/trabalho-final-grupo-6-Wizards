#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from sys import displayhook
from core.Actor import Actor
import math


class Mago(Actor):
    def __init__(self, idx: int,life_max: int, lista_magias: list,
                 dano_base: int, ang: float, grupo, Image_dict: dict, 
                 acc_ang=5, accel=0.5, atr=0.99):
        self.__idx = idx
        self._life_max =life_max
        self.__lista_magias = lista_magias
        self.__dano_base = dano_base
        self.__accel = accel
        self.__life =life_max
        self.__slots = [None, None, None]
        self.__effects = [self.damage(2)]
        self.__atr = atr
        super().__init__(radius=25, image_dict=Image_dict, size=(50, 50),
                         ang=ang, vel=(0, 0), groups=grupo)
        self.__vivo = True
        self.__impulse = False
        self.__acc_ang = acc_ang
        self.__vel_ang = 5
        self.__rotacionando = False
        self.__sentido_horario = False
        self.calc_angle_vector()

    @property
    def idx(self):
        return self.__idx

    @property
    def life_max(self):
        return self._life_max

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
    def life(self):
        return self._life

    life.setter
    def life(self,life: int):
        self._life =life

    @property
    def slots(self):
        return self.__slots

    @property
    def efeitos(self):
        return self.__efeitos

    @efeitos.setter
    def efeitos(self, efeitos: list):
        self.__efeitos = efeitos

    @property
    def vivo(self):
        return self.__vivo

    @vivo.setter
    def vivo(self, vivo: bool):
        self.__vivo = vivo

    def jogarMagia(self, n_slot: int):
        self.lista_magias[n_slot].cast(self)
        print(self.rect.center)
        print(self.rect)
        

    def acelerar(self):
        self.__impulse = True

    def rotacionar(self, sentido_horario: bool):
        self.__rotacionando = True
        self.__sentido_horario = sentido_horario

    def update(self,dt):
        if self.__rotacionando:
            if self.__sentido_horario:
                self.ang -= self.__vel_ang
            else:
                self.ang += self.__vel_ang
            self.__rotacionando = False

        if self.__impulse:  # mover para frente se ha impulso
            new_vel = (self.vel[0] + self.angle_vector[0] * self.__accel,
                       self.vel[1] + self.angle_vector[1] * self.__accel)
            self.__impulse = False
        else:
            new_vel = self.vel

        # perda de velocidade por atrito:
        self.vel = (new_vel[0]*self.__atr, new_vel[1]*self.__atr)

        for effect in self.__effects:
            effect(self)

        super().update(dt)  # tem q passar dt

    def add_efects (self, effect):
        self.__effects.append(effect)

        
    def damage(self, damage):
        if self.protection() in self.__effects:
            pass
        else:
            self.life -= damage 


    



        

