#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create a html-page from bookmarks of a xml-files.
Sort files dependent of the category.

An '&' in an url doesn't work because of the xml-file.
"""

import webbrowser

from lxml import etree

# get content from xml
xmlpath = "/home/kame/Dropbox/data/links.xml"
xml = etree.parse(xmlpath)
# print(etree.tostring(xml))

# todo - sort for category
# convert data structure and save data in html-file
url = "/tmp/links.html"
f = open(url, "w")
f.write("<html>")
f.write("<head>")
f.write("</head>")
f.write("<body>")
f.write("My bookmarks:\n\n")
for i in range(1, 11):
    f.write("<a href=\"" + str(xml.xpath("//item[" + str(i) + "]/url/text()")[0]) + "\">abc</a>\n")
f.write("</body>")
f.write("</html>")

# open html-file
new = 2  # open in a new tab, if possible
webbrowser.open(url, new=new)