# coding=utf-8

import random

import lex_analyse_tags
import lex_count_tags
import lex_sort
import linux
import podcast_to_dropbox
import remove_pyc

print("remove_pyc()")


remove_pyc.main()

print("lex_analyse_tags()")


lex_analyse_tags.main()

print("lex_count_tags()")

lex_count_tags.main()

rnd = random.randint(1, 8)
if rnd == 1:
    print("lex_sort()")
    lex_sort.main()

print("podcast_to_dropbox()")

podcast_to_dropbox.get_podcasts()

rnd = random.randint(1, 20)
if rnd == 1:
    print("update_system()")

    linux.update_system()
