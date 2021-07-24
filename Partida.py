import pygame as pg
from Mago import Mago
import time 

from pygame.constants import K_0

class Partida():

    def __init__(self, canvas, window):
        self.canvas = canvas
        self.window = window

        self.Redefinir()
    def Redefinir(self):
        self.M_grupo = pg.sprite.Group()

        Mage_image = pg.Surface((80, 80), pg.SRCALPHA)
        pg.draw.circle(Mage_image, (255, 0, 0), (40, 40), 40)
        M_image_dict = {'bola': Mage_image}

        self.MagoTest = Mago(0, 0, [], 2, 1, self.M_grupo, M_image_dict)

    def run(self):
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

            for event in pg.event.get():

                if event.type == pg.QUIT:

                    running = False

            keys = pg.key.get_pressed()
            if keys[K_0]:
                self.MagoTest.acelerar()

            self.canvas.fill((0, 200, 200))

            self.MagoTest.update(self.canvas, dt, (0, 0))
            self.M_grupo.draw(self.canvas)

            self.window.blit(self.canvas, (0, 0))
            pg.display.update()

