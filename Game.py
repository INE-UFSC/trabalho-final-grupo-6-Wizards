#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg

from gerenciadores.Config import Config
from gerenciadores.estados.Estado import Estado
from gerenciadores.estados.Menu import Menu
from gerenciadores.estados.Partida import Partida


class Game():
    def __init__(self):
        pg.init()

    def run(self):
        self.config = Config()
        # Janela
        self.window = pg.display.set_mode(self.config.screen_size)

        # Controle de tempo
        self.clock = pg.time.Clock()

        # Estados do jogo
        self.estados_enum = {"Menu": 0, "Partida": 1}
        menu = Menu(self.window, self.config)
        partida = Partida(self.window, self.config)
        self.estados: list[Estado] = [menu, partida]
        self.e = 1  # estado atual

        partida.Iniciar(n_players=1)  # Inicia a partida

        run = True
        while run:
            self.estados[self.e].display()
            self.clock.tick(self.config.FPS)
            if pg.event.get(eventtype=pg.QUIT):
                if self.e == 1:
                    run = False
                else:
                    self.e += 1
            self.estados[self.e].run()
        print("end")
        pg.display.quit()
