#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto

    Gerencia a partida
"""
import pygame as pg
# import time
from pygame.constants import K_0

from gerenciadores.Inputs import Inputs
from gerenciadores.estados.Estado import Estado
from core.Mago import Mago


class Partida(Estado):
    def Redefinir(self):
        self.M_grupo = pg.sprite.Group()

        Mage_image = pg.Surface((80, 80), pg.SRCALPHA)
        pg.draw.circle(Mage_image, (255, 0, 0), (40, 40), 40)
        width = 6
        pg.draw.rect(Mage_image, (0, 255, 0),
                     pg.Rect(40, 40-width/2, 40, width))
        M_image_dict = {'bola': Mage_image}

        self.Magos = [Mago(idx=0, vida_max=10, lista_magias=[], dano_base=2,
                           ang=315, grupo=self.M_grupo, accel=5,
                           Image_dict=M_image_dict)]

        self.inputs = Inputs(self.config.p0)

    def Iniciar(self, n_players: int = 1):
        self.__n_players = n_players
        self.Redefinir()

    def __process_inputs(self):
        actions = self.inputs.get()
        for p in range(self.__n_players):
            if 0 in actions[p]:  # turn_r
                if 1 not in actions[p]:  # not turn_l
                    self.Magos[p].rotacionar(True)
            elif 1 in actions[p]:  # turn_l
                self.Magos[p].rotacionar(False)

            if 2 in actions[p]:  # acc
                if 3 not in actions[p]:  # dacc
                    self.Magos[p].acelerar()
            elif 3 in actions[p]:  # dacc
                pass  # desacelerar

            if 4 in actions[p]:  # slot0
                pass
            if 5 in actions[p]:  # slot1
                pass
            if 6 in actions[p]:  # slot2
                pass
            if 7 in actions[p]:  # slot3
                pass

    def run(self):
        self.__process_inputs()

        self.canvas.fill((0, 200, 200))

        for p in range(self.__n_players):
            self.Magos[p].update()
        self.M_grupo.draw(self.canvas)
        return 1
