# coding=utf-8

"""
simulate a mouse
move to position
click position

only works in linux
"""

import os


def set_position(x: int, y: int) -> object:
    os.system("xte 'mousemove " + str(x) + " " + str(y) + "'")


def watch_position():
    # os.system("xdotool getmouselocation")
    os.system("watch xdotool getmouselocation")  # watch live
    # os.system("xdotool getmouselocation 2>/dev/null | cut -d\  -f1,2 -")

def click():
    os.system("xte 'mouseclick 1'")
