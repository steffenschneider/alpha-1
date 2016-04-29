# coding=utf-8

"""
simulate a mouse
move to position
click position

only works in linux
"""

import os

def position(x: int, y: int) -> object:
    os.system("xte 'mousemove " + str(x) + " " + str(y) + "'")

def click():
    os.system("xte 'mouseclick 1'")
