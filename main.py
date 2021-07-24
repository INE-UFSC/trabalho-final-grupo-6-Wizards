import pygame as pg


from pygame.constants import K_0
from gerenciador import Gerenciador
from Mago import Mago
from Menu import Menu
from Partida import Partida


pg.init()  # inicia pggame
DISPLAY_W, DISPLAY_H = 900, 500
canvas = pg.Surface((DISPLAY_W+500, DISPLAY_H+500))
window = pg.display.set_mode(((DISPLAY_W, DISPLAY_H)))



# Controle de tempo
menu = Menu(canvas, window)
partida = Partida(canvas,window)
f = 0

run = True
while run:
    for event in pg.event.get():

            if event.type == pg.QUIT:

                run = False
    menu.run()
partida.run()

