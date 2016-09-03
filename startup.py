# coding=utf-8

import random

import backlight_dependent_on_time
import lex_sort
import linux
import podcast_to_dropbox
import remove_pyc
import wortschatz
import xml_to_html

rnd = random.randint(1, 8)
if rnd == 1:
    print("lex_sort()")
    lex_sort.main()

rnd = random.randint(1, 20)
if rnd == 1:
    print("update_system()")
    linux.update_system()

rnd = random.randint(1, 3)
if rnd == 1:
    print("xml to html")
    xml_to_html.main()

remove_pyc.main()
wortschatz.main()
podcast_to_dropbox.get_podcasts()
backlight_dependent_on_time.main()
