# coding=utf-8

from f import get_battery_status_in_percent, check_wlan, check_sleeping_time, sort_f_py, get_todo_without_future
from repeating_helper import lex_sort, remove_pyc, linux, backlight_dependent_on_time
from repeating_helper import lex_spell_checker, lex_duplicates, wortschatz, lex_analyse_tags, backup
from repeating_helper import pip_updater, lex_link_maker, lex_check_size


def main():
    backlight_dependent_on_time.main()
    check_wlan()
    check_sleeping_time()
    get_battery_status_in_percent()
    remove_pyc.main()
    lex_sort.main()
    lex_check_size.main()
    wortschatz.delete_duplicates()
    lex_spell_checker.main()
    lex_duplicates.main()
    lex_analyse_tags.main()
    lex_link_maker.main()
    backup.main()
    linux.update_system()
    pip_updater.main()
    sort_f_py()
    get_todo_without_future()
    print("SYSTEM IS CHECKED AND UPDATED")

if __name__ == '__main__':
    main()
