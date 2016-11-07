from subprocess import call

import f

"""
Backlight-adjuster
Change the display light according to the time.
Works only on Linux.
"""


def main():
    minute_of_the_day = int(f.get_minute_of_the_day())
    if minute_of_the_day < 7 * 60:
        call(["xbacklight", "-set", "7"])
    if 7 * 60 < minute_of_the_day < 9 * 60:
        call(["xbacklight", "-set", "50"])
    if 9 * 60 < minute_of_the_day < 19 * 60:
        call(["xbacklight", "-set", "90"])
    if 19 * 60 < minute_of_the_day < 20 * 60:
        call(["xbacklight", "-set", "24"])
    if 20 * 60 <= minute_of_the_day < 20.5 * 60:
        call(["xbacklight", "-set", "14"])
    if 20.5 * 60 <= minute_of_the_day < 21 * 60:
        call(["xbacklight", "-set", "11"])
    if 21 * 60 <= minute_of_the_day < 22 * 60:
        call(["xbacklight", "-set", "7"])
    if 22 * 60 <= minute_of_the_day < 23 * 60:
        call(["xbacklight", "-set", "4"])
    if 23 * 60 <= minute_of_the_day < 24 * 60:
        call(["xbacklight", "-set", "3"])

if __name__ == '__main__':
    main()
