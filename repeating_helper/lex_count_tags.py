# coding=utf-8

"""
Count all tags in square brackets after a blank line and sort them
"""


def main():
    import re
    import os
    from collections import Counter

    # open file
    if os.name == 'nt':  # Windows
        file_ = r"C:\Users\kame\Dropbox\main-lex.txt"
    else:
        file_ = "/home/kame/Dropbox/main-lex-work.txt"
    with open(file_) as f:
        content = f.readlines()

    found_empty = 0
    lst = []

    for i in range(len(content)):
        # print(content[i])
        # '\r\n' unter virtueller Maschine + Linux, sonst '\n'
        if content[i] == "\r\n" or content[i] == "\n":
            found_empty = 1
        if found_empty > 0:
            found_empty += 1

        # get tags two line behind an empty line
        if found_empty == 4:
            if re.search(r"^\[.{0,90}\]", content[i]):
                found_empty = 0
                mo = re.search(r"^\[.{0,90}\]", content[i])
                lst.append(mo.group()[1:-1])

    c = Counter(lst)
    for letter, count in c.most_common(111):
        print(str(letter) + (20 - len(letter)) * ' ' + '\t' + str(count))


if __name__ == '__main__':
    main()
