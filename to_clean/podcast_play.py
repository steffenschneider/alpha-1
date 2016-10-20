# coding=utf-8

"""
Open a list with podcasts.
Write a number and choose a podcast.
Then play the podcast.
"""

import collections
import re
import webbrowser

import requests

import mydata

podcast_links_dict = mydata.podcast_links_dict

# sort dict
podcast_links_dict_ordered = collections.OrderedDict(sorted(podcast_links_dict.items()))

# print all available podcasts
print("Choose a podcast: ")
for i in range(len(podcast_links_dict_ordered)):
    print(str(i + 1) + " " + str(list(podcast_links_dict_ordered.keys())[i]))

# get user input
choice = input('Your choice: ')

# open podcast
url = str(list(podcast_links_dict_ordered.values())[int(choice) - 1])

# choose first mp3-link
response = requests.get(url)
content_binary = response.content
content_ = content_binary.decode('utf-8')
items = re.findall("<guid>(http://.+_.+\.mp3)", content_)

# load first mp3-url
mp3_url = items[0].split('\"')[0]
new = 2  # open in a new tab, if possible
webbrowser.open(mp3_url, new=new)
