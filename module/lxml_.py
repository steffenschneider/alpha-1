#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Often used function for extracting data from a XML-file.

This file is not ready yet.
"""

# from lxml import etree
import xml.etree.ElementTree as ET


def parse_xml(topic):
    xmlpath = ''
    if topic == 'contacts':
        xmlpath = "/home/kame/Dropbox/data/contacts.xml"
    if topic == 'music':
        xmlpath = "/home/kame/Dropbox/data/music.xml"
    else:
        print("Error: topic not found")
    xml_ = ET.parse(xmlpath)
    return xml_


def print_whole_xml(xml_):
    print(ET.tostring(xml_))


def count_items(xpath):
    n_items = len(xml.xpath(xpath))
    print(str(n_items) + " items")
    return n_items


def item_attributes(xml_):
    # show attributes between the item tag
    import re
    # print(etree.tostring(xml))
    lst = re.findall(r'<\/?(.*?)\/?>', ET.tostring(xml_))
    # print(lst)

    # count all tags
    print("number of tags: " + str(len(lst)))
    from collections import Counter
    c = Counter(lst)
    taglist = []
    # print("most used attributes: " + str(c.most_common(4)[0][0]) + ", " +
    #  str(c.most_common(4)[1][0]) + ", " + str(c.most_common(4)[2][0]))
    for letter, count in c.most_common(15):
        # print('%s: %7d' % (letter, count))
        taglist.append(letter)
    # print all existing tags
    taglist = list(set(taglist))
    # first word is outer tag
    print("most outer tag: " + lst[0])
    taglist.remove(lst[0])
    # print(taglist)
    # second word depicts every item
    print("item tag (e.g. item): " + lst[1])
    taglist.remove(lst[1])
    # show attributes
    print("attributes: " + str(taglist))


xml = parse_xml('contacts')
# print_whole_xml(xml)
# count_items(xml)
item_attributes(xml)
# get_y_if_x_equal_xx(xml)  # todo

# print all artists
# print(xml.xpath("//artist/text()"))
# print first artist
# print(xml.xpath("//item[1]/artist/text()"))
# print all song titles
# print(xml.xpath("//song/text()"))

# n_songs
# print(str(len(xml.xpath("//song/text()"))) + " songs")

# artist = 'Arovane'
# for i in range(1, n_items+1):
#    temp = str(xml.xpath("//item[" + str(i) + "]/artist/text()"))
#    if temp[2:-2] == artist:
#        print("Artist '" + str(artist) + "' found at position " + str(i))
#        print("Song of this artist: " + str(xml.xpath("//item[" + str(i) + "]/song/text()"))[2:-2])

if __name__ == '__main__':
    pass
    # print_whole_xml(sys.argv[1])
