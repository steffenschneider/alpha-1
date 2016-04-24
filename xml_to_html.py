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

# convert data structure
# todo

# save data in html-file
# todo

# open html-file
# todo
