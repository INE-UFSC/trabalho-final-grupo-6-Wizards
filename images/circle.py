#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg
from core import RSurface


def circle(radius, color):
    img = RSurface(radius, (2*radius, 2*radius), pg.SRCALPHA)
    pg.draw.circle(img, color, (radius, radius), radius)
    return img
