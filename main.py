#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto

    Run the game
"""
from Game import Game
import pygame as pg
pg.mixer.init()
game = Game()
try:
    game.run()
except:
    pg.display.quit()
    raise
