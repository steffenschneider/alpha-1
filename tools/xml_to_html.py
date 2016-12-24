#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create a html-page from bookmarks of a xml-files.
Sort files dependent of the category.

An '&' in an url doesn't work because of the xml-file.
"""

# from lxml import etree
import xml.etree.ElementTree as ET


def main():
    # get content from xml
    xmlpath = "/home/kame/Dropbox/data/links.xml"
    tree = ET.parse(xmlpath)
    root = tree.getroot()

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

    # count bookmarks
    n_items = len(root.findall("./item"))
    print(str(n_items) + " bookmarks in the xml-file")

    # sort categories in 2D-list
    elements = []
    for i in range(n_items):
        elements.append([])

        # first column: category
        category = root.findall("./item[" + str(i + 1) + "]/category")[0].text.lower()
        elements[i].append(category)

        # second column: url
        name_ = root.findall("./item[" + str(i + 1) + "]/name")[0].text
        urltext = "<a href=\"" + str(root.findall("./item[" + str(i + 1) + "]/url")[0].text) + "\">" + str(
            name_) + "</a><br>"
        elements[i].append(urltext)

        active = root.findall("./item[" + str(i + 1) + "]/active")[0].text
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


# nav {
#     float: left;
#     max-width: 160px;
#     margin: 0;
#     padding: 1em;
# }


if __name__ == '__main__':
    main()
