#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg

from managers.Config import Config
from managers.states import State
from managers.states import Menu
from managers.states import Match


class Game():
    def __init__(self):
        pg.init()
        self.config = Config()
        self.states_enum = {"Menu": 0, "Match": 1}

    def run(self):
        # Initializa window
        self.window = pg.display.set_mode(self.config.screen_size)

        # Time control
        self.clock = pg.time.Clock()

        # Game states
        menu = Menu(self.window, self.config)
        match = Match(self.window, self.config)
        self.__states: list[State] = [menu, match]
        self.__current_state = 1

        match.Start(n_players=1)

        run = True
        while run:
            self.__states[self.__current_state].display()
            self.clock.tick(self.config.FPS)

            if pg.event.get(eventtype=pg.QUIT):
                if self.__current_state == 1:
                    run = False
                else:
                    self.__current_state += 1
            self.__states[self.__current_state].run()
        print("end")
        pg.display.quit()
