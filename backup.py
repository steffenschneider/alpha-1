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
        # if re.findall(r"([^/]+$)", s)[0][0] != ".":
        try:
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
                print('Files copied with shutil.copytree')
            else:
                shutil.copy2(s, d)
                print("Files copied with shutil.copy2")
        except RuntimeError:
            print("No files copied!!!!!!!!!!")
            pass


# todo - make a backup dependent on the usb-stick
copytree("/home/kame/lex", "/media/INTENSO/lex")
copytree("/home/kame/malen", "/media/INTENSO/malen")
copytree("/home/kame/programme", "/media/INTENSO/programme")
copytree("/home/kame/sound", "/media/INTENSO/sound")
