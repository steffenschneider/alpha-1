# coding=utf-8

import random

print("remove_pyc()")
import remove_pyc

remove_pyc.main()

print("lex_analyse_tags()")
import lex_analyse_tags

lex_analyse_tags.main()

print("lex_count_tags()")
import lex_count_tags

lex_count_tags.main()

print("lex_sort()")
import lex_sort

lex_sort.main()

print("podcast_to_dropbox()")
import podcast_to_dropbox

podcast_to_dropbox.get_podcasts()

rnd = random.randint(1, 10)
if rnd == 1:
    print("update_system()")
    import linux

    linux.update_system()
