import os


def main():
    if os.name == "posix":
        path = "/home/kame/Dropbox/"
    elif os.name == "nt":
        path = "C:/Users/steffen.schneider/dropbox/"

    size_1 = os.path.getsize(path + "main-lex.txt")
    if size_1 < 955000:
        print("main-lex.txt is to small. data loss?")
    size_2 = os.path.getsize(path + "main-lex-work.txt")
    if size_2 < 570000:
        print("main-lex-work.txt is to small. data loss?")


if __name__ == '__main__':
    main()
