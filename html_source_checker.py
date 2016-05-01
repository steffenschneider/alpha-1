# coding=utf-8

"""
Analyse html tags in the source code
Just started ...
"""

import re

import requests

# get the source code
res = requests.get('https://www.heise.de')

print("type(): " + str(type(res)))
print("res.status_code: " + str(res.status_code))  # requests.codes.ok
print("len(): " + str(len(res.text)))
# print(res.text[:2500])
# fill the tag_list with <...>
tag_list = re.findall('<[\w\d]*.[\w\d]*>', res.text)

# remove all </a>
while '</a>' in tag_list:
    tag_list.remove('</a>')

# remove all <hr>
while '<hr>' in tag_list:
    tag_list.remove('<hr>')

# show all html-tags
spaces = 0
for i in range(len(tag_list)):
    found_slash = False
    if '/' in tag_list[i]:
        found_slash = True
    if not found_slash:
        spaces += 1
    if found_slash:
        spaces -= 1
    if spaces < 0:
        spaces = 0
    print(str(i) + ' ' + spaces * ' ' + str(tag_list[i]))
