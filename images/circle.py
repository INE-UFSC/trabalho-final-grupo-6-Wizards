#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
import pygame as pg
from pygame import gfxdraw
from core import RSurface


def circle(radius, color, surface=None, pos=None):
    if surface is None:
        surface = RSurface(radius, (2*radius+2, 2*radius+2), pg.SRCALPHA)
    if pos is None:
        pos = (radius, radius)
    gfxdraw.aacircle(surface, *pos, radius, color)
    gfxdraw.filled_circle(surface, *pos, radius, color)
    return surface
