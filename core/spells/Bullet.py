#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from images import circle
from core import Spell, RSurface
import time
import pygame as pg
import os
import numpy as np


class Bullet(Spell):
    __projectile_duration = 2.5
    __target_cooldown = 0.2
    __target_duration = 1.5
    __abs_vel = 9
    __damge = 2
    __targeting_r = 1500

    def __init__(self, wizard_id: int, groups: list, screen_size: tuple):
        image_dict = {
            "projectile": {"path": os.path.join("images", "spells_img",
                                                "bullet_img.png"),
                           "R": 7, "size": (32, 32)},
            "targeting": {"image": RSurface(self.__targeting_r,
                                            (self.__targeting_r*2,
                                             self.__targeting_r*2),
                                            pg.SRCALPHA)}
        }

        sound_dict = {"casting": "bullet_sound"}

        super().__init__(
            wizard_id=wizard_id,
            name="Bullet",
            icon="bullet_icon",  # circle(Spell.icon_radius, (100, 100, 255)),+
            image_dict=image_dict,
            sound_dict=sound_dict,
            ang=0,
            screen_size=screen_size,
            groups=groups,
        )

    def cast(self, wiz):
        super().cast(wiz)
        self.ang = wiz.ang
        self.vel = (
            wiz.angle_vector[0] * self.__abs_vel,
            wiz.angle_vector[1] * self.__abs_vel,
        )
        self.state = "targeting"
        self.target = None
        self.target_dist2 = self.__targeting_r**2

    def calc_angle(self, x, y):
        ang = np.rad2deg(np.arctan(-y/x)) % 360
        if x < 0:
            ang = (ang+180) % 360
        return ang

    def update(self, dt):
        if time.time() > self.spawned_time + self.__projectile_duration:
            self.kill()

        if self.state == "targeting":
            self.state = "projectile"

        temp_ang = self.calc_angle(*self.vel)

        if (time.time() > self.spawned_time + self.__target_cooldown) and\
           (time.time() < self.spawned_time + self.__target_duration):
            target_ang = self.calc_angle(
                self.target.center[0] + self.target.vel[0] - self.center[0],
                self.target.center[1] + self.target.vel[0] - self.center[1])
            ang_dif = (target_ang-temp_ang) % 360
            if ang_dif > 180:
                ang_dif = ang_dif-360
            ang_dif = min(max(ang_dif, -5), 5)
            self.ang = (temp_ang + ang_dif) % 360
            self.vel = (
                self.angle_vector[0] * self.__abs_vel,
                self.angle_vector[1] * self.__abs_vel,
            )
            print("bullet:", temp_ang)
            print("target:", target_ang)
            print("dif:", target_ang-temp_ang)
            print("dif:", ang_dif)
            print("new_bullet:", self.ang)
            print()
            if temp_ang>360 or temp_ang<0:
                raise ValueError
        else:
            self.ang = temp_ang % 360

        super().update(1)

    def colision(self, wiz):
        if wiz.idx != self.wizard_id:
            if self.state == "targeting":
                dist2 = (self.center[0]-wiz.center[0])**2 +\
                        (self.center[1]-wiz.center[1])**2
                if dist2 < self.target_dist2:
                    self.target_dist2 = dist2
                    self.target = wiz
            else:
                wiz.damage(self.__damge)
                self.kill()
