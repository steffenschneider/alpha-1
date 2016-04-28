# coding=utf-8

"""
Check the html source code for id-tags
"""

import requests
import re


def run(url):

    # check link syntax
    if url[:4] != 'http' and url[:3] != 'www':
        url = 'http://www.' + str(url)
    if url[:4] != 'http':
        url = 'http://' + str(url)
    if url[-1:] != '/':
        url += '/'

    # get content
    response = requests.get(url)
    content_binary = response.content
    content_ = content_binary.decode('utf-8')
    items = re.findall("id=\"(.+)", content_)

    # show items
    for elem in items:
        print(elem.split('\"')[0])

if __name__ == "__main__":
    import sys
    run(sys.argv[1])
