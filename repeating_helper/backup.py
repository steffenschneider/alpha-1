# coding=utf-8

"""
Copy a file from source to destination.
At first all files at the destination will be deleted.
"""

import os
import shutil


def copytree(src, dst, symlinks=False, ignore=None):
    # if destination folder exists, you can't copy the files
    # therefore at first delete the destination
    try:
        shutil.rmtree(dst)
    except FileNotFoundError:
        pass

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        try:
            if os.path.isdir(s):  # if dir exist
                shutil.copytree(s, d, symlinks, ignore)
                print('Files copied with shutil.copytree')
            else:
                shutil.copy2(s, d)
                print("Files copied with shutil.copy2")
        except RuntimeError:
            print("No files copied!")
            pass


input("Insert USB and press Enter:")

# Dropbox files
print("copy Dropbox")
copytree("/home/kame/Dropbox", "/media/kame/TOSHIBA EXT/Steffen/Dropbox")

# Desktop files
print("copy main")
copytree(r"/home/kame/Desktop/main", "/media/kame/TOSHIBA EXT/Steffen/main")
# print("copy bilder")
# copytree(r"/home/kame/Desktop/main/bilder", "/media/kame/TOSHIBA EXT/Steffen/bilder")
# print("copy mp3")
# copytree(r"/home/kame/Desktop/main/mp3", "/media/kame/TOSHIBA EXT/Steffen/mp3")
# print("copy wichtig")
# copytree(r"/home/kame/Desktop/main/wichtig", "/media/kame/TOSHIBA EXT/Steffen/wichtig")
