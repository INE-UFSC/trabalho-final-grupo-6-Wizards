import pygame as pg
from Mago import Mago

pg.init() #inicia pggame
DISPLAY_W, DISPLAY_H = 900, 500
canvas = pg.Surface((DISPLAY_W+500,DISPLAY_H+500))
window = pg.display.set_mode(((DISPLAY_W,DISPLAY_H)))

imagens = {'image': 0}
MagoTest = Mago(0,3,[],2,3,40,imagens,(30,30),10)
running = True
while running:
    for event in pg.event.get():
            
        if event.type == pg.QUIT:
    
            running = False