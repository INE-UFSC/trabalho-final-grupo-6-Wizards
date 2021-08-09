#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto

    Classe base para as magias
"""
import pygame as pg

from gerenciadores.Config import PlayerConf


class Inputs():
    def __init__(self, *players: PlayerConf):
        self.__n_players: int = len(players)
        self.__players: tuple[PlayerConf, ...] = players
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
        self.__inputs: dict[int, list[tuple[int, int]]] = {}
        for player in range(self.__n_players):
            player_command: list[int] = self.__players[player].list_form
            for com in range(len(player_command)):
                if player_command[com] in self.__inputs:
                    self.__inputs[player_command[com]].append((player, com))
                else:
                    self.__inputs[player_command[com]] = [(player, com)]

    def get(self) -> list[list[str]]:
        pressed: list[list[str]] = [[]]*self.__n_players
        for event in pg.event.get(eventtype=pg.KEYDOWN):
            if event.key in self.__inputs:
                for player, command in self.__inputs[event.key]:
                    pressed[player].append(command)
        return pressed
