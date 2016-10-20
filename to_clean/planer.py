# coding=utf-8

import datetime
import time

# Programm zur Plannung aller Aufgaben und auch der Freizeit
# Abfrage: Freier Tag?
# Log anfertigen für Statistik

print("Freier Tag?")
freetime_flag = 0
a = input()
if a == 'y' or a == 'ye' or a == 'yes' or a == '1':
    print("Freier Tag\n")
    freetime_flag = 1
else:
    print("Arbeitstag\n")
    freetime_flag = 0

children_flag = 0
if freetime_flag == 1:
    print("Auf Kind aufpassen?")
    a = input()
    if a == 'y' or a == 'ye' or a == 'yes' or a == '1':
        print("Auf Kind aufpassen!\n")
        children_flag = 1
    else:
        print("Nicht auf Kind aufpassen!\n")
        children_flag = 0

for i in range(11111):
    # log data
    task = input("Aktuelle Aufgabe?\n")
    with open(r"/home/kame/Dropbox/data/planer_log.txt", "a") as myfile:
        # write datetime
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%d.%m.%Y %H:%M:%S')
        myfile.write(str(st))
        myfile.write("\t")
        myfile.write("freetime_flag: " + str(freetime_flag) + "\t")
        myfile.write("children_flag: " + str(children_flag) + "\t")
        myfile.write("task: " + str(task))
        myfile.write("\n")

    time.sleep(15 * 60)
