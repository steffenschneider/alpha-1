# coding=utf-8

"""
Create random strings
"""

import random
import re

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
         'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z',
         '_', '!']
list2 = []
Nzeichen = len(list_)
laenge = 80
for i in range(laenge):
    x = int(random.randint(0, Nzeichen - 1))
    list2.append(list_[x])

z = str(''.join(str(i) for i in list2))
print(z)
print(re.sub("(..........)", "\\1\n", z))  # Breite entspricht Anzahl der Punkte
