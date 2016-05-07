#!/usr/bin/env python
# -*- coding: utf-8 -*-
# later - ask for category

import random
import time

while 1:
    category = ['Arbeit', 'Astronomie', 'Computer',
                'Gehirn', 'Geschichte', 'Persönlichkeit', 'Physiologie',
                'Politik', 'Psychologie', 'Python', 'Rest', 'Testing',
                'Testprogramm', 'Tier', 'Wirtschaft']

    # read file content
    path = "/home/kame/Dropbox/"
    filename = "main-lex.txt"
    file_ = path + filename
    file_input = open(file_, "r")
    text = file_input.readlines()  # .read() read only one line

    # choose item
    # count articles --> with ##
    counter = 0
    for i in range(len(text)):
        if text[i][:2] == '##':
            counter += 1

    # find article position
    found = 0
    while found == 0:
        count = 0
        pos = 0

        # random number
        rnd = random.randint(0, counter)

        for i in range(len(text)):
            if text[i][:2] == '##':
                count += 1
                # print(rnd)
                if count == rnd:
                    if text[i + 1][1:-2] in category:
                        pos = i
                        found = 1

    # show random article
    for i in range(44):
        print("")
    end = 0
    while end == 0:
        print(text[pos][:-1])
        pos += 1
        if text[pos] == "\r\n" or text[pos] == "\n":
            end = 1
    print("")

    time.sleep(25)
