
import os
import glob

def run():
    print('Remove the .pyc files in the Python-script folder')
    filepath = "/home/kame/Dropbox/code/python/scripts/*.pyc"
    for file in glob.glob(filepath):
        print("remove " + str(file))
        os.remove(file)

if __name__ == '__main__':
    run()
