# coding=utf-8

from repeating_helper import lex_sort, remove_pyc, linux, backlight_dependent_on_time
from repeating_helper import lex_spell_checker, lex_duplicates, wortschatz, lex_analyse_tags, backup

remove_pyc.main()
lex_sort.main()
backlight_dependent_on_time.main()
wortschatz.delete_duplicates()
lex_spell_checker.main()
lex_duplicates.main()
lex_analyse_tags.main()
backup.main()
linux.update_system()

print("SYSTEM IS CHECKED AND UPDATED")
