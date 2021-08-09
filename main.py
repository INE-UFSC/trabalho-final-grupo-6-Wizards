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

config = Config()
pg.init()

# Janela
window = pg.display.set_mode(config.screen_size)

# Controle de tempo
clock = pg.time.Clock()

# Estados do jogo
estados_enum = {"Menu": 0, "Partida": 1}
estados: list[Estado] = [Menu(window, config), Partida(window, config)]
e = 1  # estado atual

estados[1].Iniciar(n_players = 1)  # Inicia a partida

run = True
while run:
    estados[e].display()
    clock.tick(config.FPS)
    if pg.event.get(eventtype=pg.QUIT):
        if e == 1:
            run = False
        else:
            e += 1
    estados[e].run()
print("end")
pg.display.quit()
