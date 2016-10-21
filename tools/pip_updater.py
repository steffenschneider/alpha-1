import os
import re
import subprocess

sudo_password = input("password:")

# update all python 2.x modules
tasks = subprocess.Popen(["pip2", "list", "-o"], stdout=subprocess.PIPE).communicate()[0]
tasks = tasks.decode('UTF-8').split("\n")
for elem in tasks:
    if len(elem) > 0:
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
    if len(elem) > 0:
        elem = re.findall(r"(.*?) \(", elem)[0]
    print("##########################################################")
    print("#####           installing" + str(elem))
    print("##########################################################")
    command = "pip3 install --upgrade " + str(elem)
    os.system('echo %s|sudo -H -S %s' % (sudo_password, command))
