from Game import Game
import pygame as pg


game = Game()
try:
    game.run()
except:
    pg.display.quit()
    raise
