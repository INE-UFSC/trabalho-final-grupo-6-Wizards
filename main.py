import pygame as pg
import time

from pygame.constants import K_0
from Mago import Mago


pg.init()  # inicia pggame
DISPLAY_W, DISPLAY_H = 900, 500
canvas = pg.Surface((DISPLAY_W+500, DISPLAY_H+500))
window = pg.display.set_mode(((DISPLAY_W, DISPLAY_H)))

#Grupo pro mago
grupo = pg.sprite.Group()

Mage_image = pg.Surface((80, 80), pg.SRCALPHA)
pg.draw.circle(Mage_image, (255, 0, 0), (40, 40), 40)
M_image_dict = {'bola':Mage_image}

MagoTest = Mago(0, 0, [], 2, 1, grupo,M_image_dict)

#Controle de tempo
FPS = 60
clock = pg.time.Clock()
prev_time = time.time()
dt = 0

running = True
while running:

    clock.tick(FPS)
    
    now = time.time()
    dt = (now - prev_time)*60
    prev_time = now
    print(dt)

    for event in pg.event.get():

        if event.type == pg.QUIT:

            running = False

    keys = pg.key.get_pressed()
    if keys[K_0]:
        MagoTest.acelerar()

    canvas.fill((0, 200, 0))
    
    MagoTest.update(canvas, dt, (0, 0))
    grupo.draw(canvas)

    window.blit(canvas, (0, 0))
    pg.display.update()
