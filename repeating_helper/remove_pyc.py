import glob
import os


def main():
    filepath = "/home/kame/Dropbox/code/python/scripts/*.pyc"
    for file in glob.glob(filepath):
        os.remove(file)

if __name__ == '__main__':
    main()
