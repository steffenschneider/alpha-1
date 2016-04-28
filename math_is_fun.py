#!/usr/bin/env python3
# coding: utf-8

# Author: Steffen Schneider und Erik Streb del Toro
# Licence: GPL v3 or newer
# Changelog:
#   - 2016-04-28: first version

"""
Math game for children of the age 5-7.
"""

# TODO
# generate random numbers    5 min
# get user input             5 min
# scoring                    5 min

import matplotlib.pyplot as plt

plt.plot([0, 1], [0, 0])
font_size = 70
plt.text(0.33, 0.02, r'1+1', fontsize=font_size)
plt.text(0.3, -0.04, r'2', fontsize=font_size)
plt.text(0.6, -0.04, r'3', fontsize=font_size)

plt.show()
