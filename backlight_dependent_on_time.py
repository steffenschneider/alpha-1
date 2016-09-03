from subprocess import call

import f


def main():
    minute_of_the_day = int(f.get_minute_of_the_day())
    print(minute_of_the_day)
    if minute_of_the_day < 400:
        call(["xbacklight", "-set", "7"])
    if 400 < minute_of_the_day < 1100:
        call(["xbacklight", "-set", "90"])
    if 1000 < minute_of_the_day < 1100:
        call(["xbacklight", "-set", "15"])
    if 1100 <= minute_of_the_day < 1200:
        call(["xbacklight", "-set", "10"])
    if 1200 <= minute_of_the_day < 1300:
        call(["xbacklight", "-set", "7"])
    if 1300 <= minute_of_the_day < 1440:
        call(["xbacklight", "-set", "4"])


if __name__ == '__main__':
    main()
