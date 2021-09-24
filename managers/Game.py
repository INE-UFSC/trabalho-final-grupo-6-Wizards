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
from managers.states import Menu
from managers.states import Match
from managers.states import Options
from managers.states import Gameover
from enum import Enum


class StatesEnum(Enum):
    Menu = 0
    Match = 1
    Options = 2
    Gameover = 3
    Exit = -1


class Game():
    states_enum = StatesEnum

    def __init__(self):
        pg.init()
        pg.font.init()  # you have to call this at the start,
        self.config = Config(os.path.join("data", "config.json"))

    def run(self):
        # Initializa window
        self.window = pg.display.set_mode(self.config.screen_size)

        # Game states
        menu = Menu(self, 'menu')
        match = Match(self, 'match')
        options = Options(self, 'options')
        gameover = Gameover(self, 'gameover')
        self.__states: dict = {
            self.states_enum.Menu: menu,
            self.states_enum.Match: match,
            self.states_enum.Options: options,
            self.states_enum.Gameover: gameover
        }

        # Time control
        self.clock = pg.time.Clock()
        for state in self.__states.values():
            state.redefine()
        self.__current_state = self.states_enum.Menu
        self.__states[self.__current_state].Start()

        while self.__current_state is not self.states_enum.Exit:
            self.__states[self.__current_state].display()
            self.clock.tick(self.config.FPS)

            if pg.event.get(eventtype=pg.QUIT):
                break

            next_state = self.__states[self.__current_state].run()

            if not (next_state is None):
                self.__current_state = next_state
                if self.__current_state == self.states_enum.Match:
                    self.__states[self.states_enum.Match].Start(
                        self.__states[self.states_enum.Menu].players)
                elif self.__current_state == self.states_enum.Gameover:
                    self.__states[self.states_enum.Gameover].Start(
                        self.__states[self.states_enum.Match].deaths)
                elif self.__current_state == self.states_enum.Menu:
                    self.__states[self.__current_state].Start()

        pg.display.quit()
