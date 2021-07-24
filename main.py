import pygame as pg


from pygame.constants import K_0
from gerenciador import Gerenciador
from Mago import Mago


pg.init()  # inicia pggame
DISPLAY_W, DISPLAY_H = 900, 500
canvas = pg.Surface((DISPLAY_W+500, DISPLAY_H+500))
window = pg.display.set_mode(((DISPLAY_W, DISPLAY_H)))

# Grupo pro mago
grupo = pg.sprite.Group()

Mage_image = pg.Surface((80, 80), pg.SRCALPHA)
pg.draw.circle(Mage_image, (255, 0, 0), (40, 40), 40)
M_image_dict = {'bola': Mage_image}

MagoTest = Mago(0, 0, [], 2, 1, grupo, M_image_dict)

# Controle de tempo
Grc = Gerenciador(canvas, window)
f = 0

run = True
while run:
    for event in pg.event.get():

            if event.type == pg.QUIT:

                run = False
    Grc.Menu()
Grc.partida()
