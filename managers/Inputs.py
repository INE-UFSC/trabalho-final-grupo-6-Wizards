#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg

from managers.Config import PlayerConf


class Inputs():
    def __init__(self, *players: PlayerConf):
        self.__n_players: int = len(players)
        self.__players: tuple = players
        self.update()

    def update(self) -> None:
        """
            Constroí o dicionário inputs para facilitar o processamento das
        entradas de botões (método get).
            As chaves são os códigos das teclas.
            Os valores são listas de tuplas, o primeiro valor das tuplas é o
        número do jogador e o segundo é o comando correspondente ao botão
        pressionado.
        """
        self.__inputs: dict = {}
        for player in range(self.__n_players):
            player_command: list = self.__players[player].list_form
            for com in range(len(player_command)):
                if player_command[com] in self.__inputs:
                    self.__inputs[player_command[com]].append((player, com))
                else:
                    self.__inputs[player_command[com]] = [(player, com)]

    def get(self) -> list:
        pressed: list = [[] for i in range(self.__n_players)]

        keys_state = pg.key.get_pressed()
        for key in self.__inputs:
            if keys_state[key]:
                for player, command in self.__inputs[key]:
                    pressed[player].append(command)
        return pressed
