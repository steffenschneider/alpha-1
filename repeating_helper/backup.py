# coding=utf-8
import f


def main():
    device_flag = 0
    for device in f.detect_devices():
        if 'Toshiba' in device:
            device_flag = 1

    if device_flag == 1:
        """
        Copy a file from source to destination.
        At first all files at the destination will be deleted.
        """

        import os
        import shutil

        def copytree(src, dst, symlinks=False, ignore=None):
            # if destination folder exists, you can't copy the files
            # therefore at first delete the destination
            # try:
            #     shutil.rmtree(dst)
            # except FileNotFoundError:
            #     pass

            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)

                # is source folder or file ?
                folder_or_file = 0
                if os.path.isdir(s):
                    folder_or_file = 10
                    # print("folder")
                elif os.path.isfile(s):
                    folder_or_file = 20
                    # print("file")
                # check if destination exist and folder of file
                if os.path.isdir(d) or os.path.isfile(d):
                    folder_or_file += 1
                    # print("         existing")
                else:
                    folder_or_file += 2
                    # print("         not existing")

                if folder_or_file == 11:
                    # check last change time
                    if os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                        shutil.rmtree(d)
                        shutil.copytree(s, d, symlinks, ignore)
                        print(s)
                    else:
                        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        pass

                if folder_or_file == 21:
                    # check last change time
                    if os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                        os.remove(d)
                        shutil.copy2(s, d)
                        print(s)
                    else:
                        # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        pass

                if folder_or_file == 12:
                    shutil.copytree(s, d, symlinks, ignore)
                    print(s)

                # file
                if folder_or_file == 22:
                    shutil.copy2(s, d)
                    print(s)

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

if __name__ == '__main__':
    main()
