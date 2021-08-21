#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg
import os

from managers.Config import Config
from managers.states import State
from managers.states import Menu
from managers.states import Match
from managers.states import Options
from managers.states import Gameover


class Game():
    def __init__(self):
        pg.init()
        pg.font.init()  # you have to call this at the start,
        self.config = Config(os.path.join("data", "config.json"))
        self.states_enum = {"Menu": 0, "Match": 1}

    def run(self):
        # Initializa window
        self.window = pg.display.set_mode(self.config.screen_size)

        # Time control
        self.clock = pg.time.Clock()

        # Game states
        menu = Menu(self.window, self.config)
        match = Match(self.window, self.config)
        options = Options(self.window, self.config)
        gameover = Gameover(self.window, self.config)
        self.__states: list[State] = [menu, match, options, gameover]
        self.__current_state = 0

        while self.__current_state >= 0:
            self.__states[self.__current_state].display()
            self.clock.tick(self.config.FPS)

            if pg.event.get(eventtype=pg.QUIT):
                break

            next_state = self.__states[self.__current_state].run()

            if not (next_state is None):
                self.__current_state = next_state
                if self.__current_state == 1:
                    match.Start(n_players=menu.players)
                if self.__current_state == 3:
                    gameover.Start(match.deaths)

        print("end")
        pg.display.quit()
