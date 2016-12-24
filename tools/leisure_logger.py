import random
import time

import easygui


def main():
    path = r"/home/kame/Dropbox/data/leisure_log.txt"

    while 1:
        time.sleep(60 * random.randint(5, 60))
        input_ = easygui.enterbox()
        with open(path, "a") as myfile:
            time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            myfile.write(time_string + "\t" + input_ + "\n")


if __name__ == '__main__':
    main()
