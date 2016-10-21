import os
import re
import subprocess

import f


def main():
    # check last update date
    path = "/home/kame/Dropbox/data/pip_updater_date.txt"
    start_time = f.file_get_last_line(path)
    if f.time_diff_in_seconds(start_time, f.get_datetime()) > 3 * 24 * 3600:
        sudo_password = input("password:")

        # update all python 2.x modules
        tasks = subprocess.Popen(["pip2", "list", "-o"], stdout=subprocess.PIPE).communicate()[0]
        tasks = tasks.decode('UTF-8').split("\n")
        for elem in tasks:
            if elem != '':
                elem = re.findall(r"(.*?) \(", elem)[0]
                print("##########################################################")
                print("#####           installing " + str(elem))
                print("##########################################################")
                command = "pip2 install --upgrade " + str(elem)
                os.system('echo %s|sudo -H -S %s' % (sudo_password, command))

        # update all python 3.x modules
        tasks = subprocess.Popen(["pip3", "list", "-o"], stdout=subprocess.PIPE).communicate()[0]
        tasks = tasks.decode('UTF-8').split("\n")
        for elem in tasks:
            if elem != '':
                elem = re.findall(r"(.*?) \(", elem)[0]
                print("##########################################################")
                print("#####           installing" + str(elem))
                print("##########################################################")
                command = "pip3 install --upgrade " + str(elem)
                os.system('echo %s|sudo -H -S %s' % (sudo_password, command))

        # append date to log-file
        f.file_insert_line(path, f.file_count_lines(path), f.get_datetime() + "\n")


if __name__ == "__main__":
    main()
