#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""


def dist_sq(p1, p2):
    dx = p1[0]-p2[0]
    dy = p1[1]-p2[1]
    return dx*dx + dy*dy


def circle_colide(sprite1, sprite2):
    d_max = sprite1.radius2 + sprite2.radius2
    return dist_sq(sprite1.rect.center, sprite2.rect.center) <= d_max
