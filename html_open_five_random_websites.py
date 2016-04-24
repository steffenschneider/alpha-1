# coding=utf-8

"""
Open random links from my bookmark.xml

example of xml:
<mylinks>
  <item>
    <name>Python3 - library</name>
    <url>https://docs.python.org/3/library/index.html</url>
    <category>python</category>
    <active>true</active>     # show page only if true
    <frequency>5</frequency>  # 1 call it less often; 9 --> call it most often
  </item>
</mylinks>
"""

__author__ = "Steffen Schneider"

import random
import re
import time
import webbrowser

# get input
myhtml = r"/home/kame/Dropbox/data/links.xml"
file_input = open(myhtml)
xml = file_input.readlines()

# create 2d array
lst = []
row = 0

# xml to 2d list
for i in range(len(xml)):

    # new item
    # create new row
    if xml[i].strip()[:5] == '<item':
        # print("new item found")
        lst.append([])

    if xml[i].strip()[:5] == '<name':
        item = re.findall("<name>(.+)</name>", xml[i])
        try:
            lst[row].append(item[0])
        except:
            pass

    if xml[i].strip()[:5] == '<url>':
        item = re.findall("<url>(.+)</url>", xml[i])
        try:
            lst[row].append(item[0])
        except:
            pass

    if xml[i].strip()[:5] == '<cate':
        item = re.findall("<category>(.+)</category>", xml[i])
        try:
            lst[row].append(item[0])
        except:
            pass

    if xml[i].strip()[:5] == '<acti':
        item = re.findall("<active>(.+)</active>", xml[i])
        try:
            lst[row].append(item[0])
        except:
            pass

    if xml[i].strip()[:5] == '<freq':
        item = re.findall("<frequency>(.+)</frequency>", xml[i])
        try:
            lst[row].append(item[0])
        except:
            pass

    if xml[i].strip()[:5] == '</ite':
        # print("item finished")
        row += 1

# choose category
categories = []
for i in range(row):
    try:
        categories.append(lst[i][2])
    except:
        pass

# todo - choose category
print("all categories:")
# show unique values
print(sorted(set(categories)))

count = 0
for i in range(30):
    try:
        rnd = random.randint(0, row)
        rnd_2 = random.randint(0, 9)

        # check if is active
        if 'false' in lst[rnd][3]:
            pass
        if 'true' in lst[rnd][3]:
            if int(lst[rnd][4]) > int(rnd_2):  # regard the frequency
                url = lst[rnd][1]
                print("url: " + str(url))
                if url[0:4] != 'http':
                    url = 'http://' + str(url)
                webbrowser.open(url, new=2)  # open in a new tab, if possible
                count += 1
                time.sleep(3)
                if count == 5:
                    break
            else:
                continue
    except:
        pass
        # print("xml field empty")
