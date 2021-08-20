#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto

    Classe para armazenar, carregar e salvar as configurações de inputs de
cada jogador e do programa
"""
import json
import pygame as pg


class PlayerConf():
    # falta implementar enter
    def __init__(self, turn_r="d", turn_l="a", acc="w",
                 slot0="j", slot1="k", slot2="l", pause="enter"):
        self.__turn_r: int = pg.key.key_code(turn_r)
        self.__turn_l: int = pg.key.key_code(turn_l)
        self.__acc: int = pg.key.key_code(acc)
        self.__slot0: int = pg.key.key_code(slot0)
        self.__slot1: int = pg.key.key_code(slot1)
        self.__slot2: int = pg.key.key_code(slot2)

        self.__dict_form: dict[str, int] = {
            "turn_r": self.turn_r, "turn_l": self.turn_l,
            "acc": self.acc, "slot0": self.slot0,
            "slot1": self.slot1, "slot2": self.slot2}

        self.__set_dict = {
            "turn_r": self.__set_turn_r, "turn_l": self.__set_turn_l,
            "acc": self.__set_acc, "slot0": self.__set_slot0,
            "slot1": self.__set_slot1, "slot2": self.__set_slot2}

        self.__command_list: list[str] = ["turn_r", "turn_l", "acc",
                                          "slot0", "slot1", "slot2"]

        self.__list_form: list[int] = []
        for cmd in self.__command_list:
            self.__list_form.append(self.__dict_form[cmd])

    @property
    def turn_r(self) -> int:
        return self.__turn_r

    @property
    def turn_l(self) -> int:
        return self.__turn_l

    @property
    def acc(self) -> int:
        return self.__acc

    @property
    def slot0(self) -> int:
        return self.__slot0

    @property
    def slot1(self) -> int:
        return self.__slot1

    @property
    def slot2(self) -> int:
        return self.__slot2

    def __set_turn_r(self, key):
        self.__turn_r = key

    def __set_turn_l(self, key):
        self.__turn_l = key

    def __set_acc(self, key):
        self.__acc = key

    def __set_slot0(self, key):
        self.__slot0 = key

    def __set_slot1(self, key):
        self.__slot1 = key

    def __set_slot2(self, key):
        self.__slot2 = key

    @property
    def dict_form(self) -> dict[str, int]:
        return self.__dict_form

    @property
    def list_form(self) -> list[int]:
        return self.__list_form

    @property
    def command_list(self) -> list[str]:
        return self.__command_list

    def json(self) -> dict[str, str]:
        return {key: pg.key.name(cd) for key, cd in self.dict_form.items()}

    def define_key(self, cmd, key):
        self.__dict_form[cmd] = key
        self.__set_dict[cmd] = key
        self.__list_form[self.__command_list.index(cmd)] = key


class Config():
    __def_FPS: int = 60
    __def_screen_size: tuple[int, int] = (1200, 720)
    __def_p0: PlayerConf = PlayerConf()
    __def_p1: PlayerConf = PlayerConf()
    __def_p2: PlayerConf = PlayerConf()
    __def_p3: PlayerConf = PlayerConf()

    def __init__(self, config_file: str = "data/config.json"):
        try:
            self.__config_file = config_file
            self.load(config_file)
        except FileNotFoundError:
            self.FPS: int = self.__def_FPS
            self.screen_size: tuple[int, int] = self.__def_screen_size
            self.p0: PlayerConf = self.__def_p0
            self.p1: PlayerConf = self.__def_p1
            self.p2: PlayerConf = self.__def_p2
            self.p3: PlayerConf = self.__def_p3
            self.p = [self.p0, self.p1, self.p2, self.p3]

            self.save()

    def load(self, config_file: str = "data/config.json") -> None:
        with open(config_file, "r") as file:
            loaded_config = json.load(file)

            self.FPS = loaded_config["FPS"]
            self.screen_size = loaded_config["screen_size"]
            self.p0 = PlayerConf(**loaded_config["p0"])
            self.p1 = PlayerConf(**loaded_config["p1"])
            self.p2 = PlayerConf(**loaded_config["p2"])
            self.p3 = PlayerConf(**loaded_config["p3"])
            self.p = [self.p0, self.p1, self.p2, self.p3]

    def as_dict(self) -> dict:
        return {
            "FPS": self.FPS,
            "screen_size": self.screen_size,
            "p0": self.p0.json(),
            "p1": self.p1.json(),
            "p2": self.p2.json(),
            "p3": self.p3.json(),
        }

    def save(self) -> None:
        with open(self.__config_file, "w") as file:
            json.dump(self.as_dict(), file)
