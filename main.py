#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg


from pygame.constants import K_0
from core.gerenciador import Gerenciador
from core.Mago import Mago
from core.Menu import Menu
from core.Partida import Partida


pg.init()  # inicia pggame
DISPLAY_W, DISPLAY_H = 900, 500
canvas = pg.Surface((DISPLAY_W+500, DISPLAY_H+500))
window = pg.display.set_mode(((DISPLAY_W, DISPLAY_H)))


# Controle de tempo
menu = Menu(canvas, window)
partida = Partida(canvas, window)
f = 0

run = True
while run:
    for event in pg.event.get():

        if event.type == pg.QUIT:

            run = False
    menu.run()
partida.run()
