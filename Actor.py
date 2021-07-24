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
import pygame as pg

class Actor(Sprite):
    def __init__(self, radius: float, image_dict: dict, size: tuple, framerate: float,
                 vel = (0,0),groups = None):
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
    def vel(self,vel):
        self.__vel = vel


    def update(self, tela,dt,new_pos = None):
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
        #teste 
        

        
        self.radius = 40
        #tela.blit(self.image,(self.rect.x,self.rect.y))
        #tela.blit(self.image,(0,0))
        
       
        new_pos = (self.vel[0],
                   self.vel[1])
        self.rect.move_ip(*new_pos)
   

