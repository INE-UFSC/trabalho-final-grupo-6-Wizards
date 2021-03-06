#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg
from pygame.constants import K_ESCAPE

from managers.states import State
from managers.Config import Config

from managers import Game


class Options(State):
    def __init__(self, game: Game, state_image):
        self.__myfont = pg.font.Font(
            'fonts/EquipmentPro.ttf', 30)

        super().__init__(game, state_image)
        self.__config_dict = self.config.as_dict()
        self.__controler = len(self.config.p0.command_list)
        self.__players = 4
        # def images(i): return os.path.join('images', 'menu_'+str(i)+'.png')
        # self.__menu_images = [pg.image.load(images(i)) for i in range(3)]

        self.waiting_image = self.__myfont.render(
            "press the input", False, (255, 255, 255))
        superficie = pg.Surface(self.waiting_image.get_size())
        superficie.blit(self.waiting_image, (0, 0))
        self.waiting_image = superficie

    def run(self):
        buttons = self.buttons_info[self.__p_sel][self.__sel]
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_UP:
                    self.__sel = (self.__sel-1) % self.__controler

                if event.key == pg.K_DOWN:
                    self.__sel = (self.__sel+1) % self.__controler
                if event.key == pg.K_RIGHT:
                    self.__p_sel = (self.__p_sel+1) % (self.__players)
                if event.key == pg.K_LEFT:
                    self.__p_sel = (self.__p_sel-1) % (self.__players)
                if event.key == K_ESCAPE:
                    return self.game.states_enum.Menu

                if event.key == pg.K_RETURN:

                    tecla = self.wait_for_key()

                    self.config.p[self.__p_sel].define_key(
                        buttons[1], tecla)
                    self.config.save()
                    self.__render_keys()

        self.__menu_images = self.__original_image.copy()

        pg.draw.rect(
            self.__menu_images, (200, 50, 50),
            pg.Rect(buttons[0]), width=3)
        self.canvas.blit(self.__menu_images, (0, 0))

        return None

    def redefine(self):
        self.__sel = 0
        self.__p_sel = 0
        self.__render_keys()

    def __render_keys(self):
        self.__config_dict = self.config.as_dict()
        temp_image = self.image.copy()
        #temp_image.fill((50, 250, 50))

        canvas_size = self.canvas.get_size()

        self.buttons_info = []
        self.control_info = ()

        for count in range(4):
            player = 'Player '+str(count+1)
            x = canvas_size[0]*(count/5) + 150
            temp_image.blit(self.__myfont.render(
                player, False, (0, 0, 0)), (x, 50))

            player_dict = self.__config_dict['p'+str(count)]

            y = 25
            p_buttons_info = []
            for key, value in player_dict.items():
                textsurface = self.__myfont.render(key+":", False, (0, 0, 0))
                tecla = self.__myfont.render(value, False, (0, 0, 0))
                size_text = textsurface.get_size()
                y += 80
                temp_image.blit(tecla, (x+size_text[0], y))
                temp_image.blit(textsurface, (x, y))
                pos_size = ((x, y), size_text)
                p_buttons_info.append((pos_size, key))
            self.buttons_info.append(p_buttons_info)
        textsurface = self.__myfont.render(
            "press Esc to return to menu", False, (0, 0, 0))
        temp_image.blit(textsurface, (0, 0))
        self.__original_image = temp_image.copy()

    def wait_for_key(self):
        while True:
            canvas_size = self.canvas.get_size()
            image = self.waiting_image.get_size()
            self.canvas.blit(
                self.waiting_image,
                (canvas_size[0]/2-image[0], canvas_size[1]/2-image[1]))
            self.display()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    return event.key
