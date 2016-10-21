# coding=utf-8

from f import get_battery_status_in_percent, check_wlan, check_sleeping_time
from repeating_helper import lex_sort, remove_pyc, linux, backlight_dependent_on_time
from repeating_helper import lex_spell_checker, lex_duplicates, wortschatz, lex_analyse_tags, backup


def main():
    check_wlan()
    check_sleeping_time()
    get_battery_status_in_percent()
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


if __name__ == '__main__':
    main()
