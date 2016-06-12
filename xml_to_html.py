#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create a html-page from bookmarks of a xml-files.
Sort files dependent of the category.

An '&' in an url doesn't work because of the xml-file.
"""

from lxml import etree

# get content from xml
xmlpath = "/home/kame/Dropbox/data/links.xml"
xml = etree.parse(xmlpath)
# print(etree.tostring(xml))

# todo - sort for category
# todo - check for empty xml-items
# convert xml data to html structure and save data in html-file
url = "/home/kame/Dropbox/data/links.html"
f = open(url, "w")
f.write("<html>")
f.write("<head>")
f.write('<meta charset="utf-8"/>')
f.write("</head>")
f.write("<body>")
f.write("My bookmarks:<br>")

n_items = len(xml.xpath("//item"))
print(str(n_items) + " bookmarks in the xml-file")

# sort categories in 2D-list
elements = []
for i in range(n_items):
    elements.append([])

    # first column: category
    category = str(xml.xpath("//item[" + str(i + 1) + "]/category/text()")[0])
    elements[i].append(category)

    # second column: url
    name_ = str(xml.xpath("//item[" + str(i + 1) + "]/name/text()")[0])
    urltext = "<a href=\"" + str(xml.xpath("//item[" + str(i + 1) + "]/url/text()")[0]) + "\">" + str(
        name_) + "</a><br>"
    elements[i].append(urltext)

    active = str(xml.xpath("//item[" + str(i + 1) + "]/active/text()")[0])
    elements[i].append(active)

elements = sorted(elements, key=lambda l: l[0])

# write sorted bookmarks to html
actual_category = ''
for i in range(n_items):
    if str(elements[i][0]) == actual_category:  # if new category write category header to html
        pass
    else:
        f.write('<br>')
        f.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
        f.write('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
        f.write('<font size="5">' + str(elements[i][0]).title() + '</font>')
        f.write('<br>')
        f.write('<br>')
        actual_category = elements[i][0]
    # write url
    if str(elements[i][2]) == 'false':
        f.write('<span style=\"opacity: 0.4;\">')  # high opacity for inactive urls
    f.write('<font size="3">' + str(elements[i][1]) + '</font>')
    if str(elements[i][2]) == 'false':
        f.write('</span>')

f.write("</body>")
f.write("</html>")

# open html-file
# new = 2  # open in a new tab, if possible
# webbrowser.open(url, new=new)
