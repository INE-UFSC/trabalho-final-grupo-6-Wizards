[1mdiff --git a/.spyproject/config/backups/workspace.ini.bak b/.spyproject/config/backups/workspace.ini.bak[m
[1mindex 34c3d94..4d82058 100644[m
[1m--- a/.spyproject/config/backups/workspace.ini.bak[m
[1m+++ b/.spyproject/config/backups/workspace.ini.bak[m
[36m@@ -4,7 +4,7 @@[m [msave_data_on_exit = True[m
 save_history = True[m
 save_non_project_files = False[m
 project_type = empty-project-type[m
[31m-recent_files = ['main.py', 'managers/states/Match.py', 'Game.py', 'managers/Inputs.py', 'managers/Config.py'][m
[32m+[m[32mrecent_files = ['main.py', 'core/spells/Bullet.py', 'managers/states/Match.py', 'core/GameObject.py', 'core/spells/Fireball.py', 'core/spells/Teleport.py'][m
 [m
 [main][m
 version = 0.2.0[m
[1mdiff --git a/.spyproject/config/workspace.ini b/.spyproject/config/workspace.ini[m
[1mindex 34c3d94..e2c56b9 100644[m
[1m--- a/.spyproject/config/workspace.ini[m
[1m+++ b/.spyproject/config/workspace.ini[m
[36m@@ -4,7 +4,7 @@[m [msave_data_on_exit = True[m
 save_history = True[m
 save_non_project_files = False[m
 project_type = empty-project-type[m
[31m-recent_files = ['main.py', 'managers/states/Match.py', 'Game.py', 'managers/Inputs.py', 'managers/Config.py'][m
[32m+[m[32mrecent_files = ['main.py', 'managers/states/Match.py', 'core/spells/Bullet.py', 'core/GameObject.py'][m
 [m
 [main][m
 version = 0.2.0[m
[1mdiff --git a/Game.py b/Game.py[m
[1mdeleted file mode 100644[m
[1mindex 247ba63..0000000[m
[1m--- a/Game.py[m
[1m+++ /dev/null[m
[36m@@ -1,59 +0,0 @@[m
[31m-#!/usr/bin/env python3[m
[31m-# -*- coding: utf-8 -*-[m
[31m-"""[m
[31m-@author:[m
[31m-    Lucas Yuki Imamura[m
[31m-    Maria Fernanda Bittelbrunn Toniasso[m
[31m-    Vitor Hugo Homem Marzarotto[m
[31m-"""[m
[31m-import pygame as pg[m
[31m-import os[m
[31m-[m
[31m-from managers.Config import Config[m
[31m-from managers.states import State[m
[31m-from managers.states import Menu[m
[31m-from managers.states import Match[m
[31m-from managers.states import Options[m
[31m-from managers.states import Gameover[m
[31m-[m
[31m-[m
[31m-class Game():[m
[31m-    def __init__(self):[m
[31m-        pg.init()[m
[31m-        pg.font.init()  # you have to call this at the start,[m
[31m-        self.config = Config(os.path.join("data", "config.json"))[m
[31m-        self.states_enum = {"Menu": 0, "Match": 1}[m
[31m-[m
[31m-    def run(self):[m
[31m-        # Initializa window[m
[31m-        self.window = pg.display.set_mode(self.config.screen_size)[m
[31m-[m
[31m-        # Time control[m
[31m-        self.clock = pg.time.Clock()[m
[31m-[m
[31m-        # Game states[m
[31m-        menu = Menu(self.window, self.config)[m
[31m-        match = Match(self.window, self.config)[m
[31m-        options = Options(self.window, self.config)[m
[31m-        gameover = Gameover(self.window, self.config)[m
[31m-        self.__states: list[State] = [menu, match, options, gameover][m
[31m-        self.__current_state = 0[m
[31m-[m
[31m-        while self.__current_state >= 0:[m
[31m-            self.__states[self.__current_state].display()[m
[31m-            self.clock.tick(self.config.FPS)[m
[31m-[m
[31m-            if pg.event.get(eventtype=pg.QUIT):[m
[31m-                break[m
[31m-[m
[31m-            next_state = self.__states[self.__current_state].run()[m
[31m-[m
[31m-            if not (next_state is None):[m
[31m-                self.__current_state = next_state[m
[31m-                if self.__current_state == 1:[m
[31m-                    match.Start(n_players=menu.players)[m
[31m-                if self.__current_state == 3:[m
[31m-                    gameover.Start(match.deaths)[m
[31m-[m
[31m-        print("end")[m
[31m-        pg.display.quit()[m
