#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from core.Actor import Actor
import math


class Mago(Actor):
    def __init__(self, idx: int, vida_max: int, lista_magias: list,
                 dano_base: int, ang: float, grupo, Image_dict: dict, 
                 acc_ang=5, accel=0.5, atr=0.95):
        self.__idx = idx
        self.__vida_max = vida_max
        self.__lista_magias = lista_magias
        self.__dano_base = dano_base
        self.__accel = accel
        self.__vida = vida_max
        self.__slots = [None, None, None]
        self.__efeitos = {}
        self.__atr = atr
        super().__init__(radius=40, image_dict=Image_dict, size=(80, 80),
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

    @vida.setter
    def vida(self, vida: int):
        self.__vida = vida

    @property
    def slots(self):
        return self.__slots

    @property
    def efeitos(self):
        return self.__efeitos

    @efeitos.setter
    def efeitos(self, efeitos: dict):
        self.__efeitos = efeitos

    @property
    def vivo(self):
        return self.__vivo

    @vivo.setter
    def vivo(self, vivo: bool):
        self.__vivo = vivo

    def jogarMagia(self, n_slot: int):
        pass

    def acelerar(self):
        self.__impulse = True

    def rotacionar(self, sentido_horario: bool):
        self.__rotacionando = True
        self.__sentido_horario = sentido_horario

    def update(self):
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
        super().update(1)  # tem q passar dt
