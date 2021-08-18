#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:
    Lucas Yuki Imamura
    Maria Fernanda Bittelbrunn Toniasso
    Vitor Hugo Homem Marzarotto
"""
from pygame import Surface


class RSurface(Surface):
    def __init__(self, r: float, *args, **kwargs):
        self.radius = r
        super().__init__(*args, **kwargs)

    @property
    def size(self):
        return self.get_size()
