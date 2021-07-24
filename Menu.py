import pygame as pg
import os

class Menu():

    def __init__(self, canvas, window):
        self.canvas = canvas
        self.window = window
        self.menu_images = [pg.image.load(os.path.join('images','menu_'+str(i)+'.png')) for i in range(3) ]


        self.testVar = 0

    def run(self):
        
        self.testVar+=1
        if self.testVar > 2:
            self.testVar = 0
        self.canvas.blit(self.menu_images[self.testVar],(0,0))
        self.window.blit(self.canvas,(0,0))
        pg.display.update()
