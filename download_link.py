# coding=utf-8

"""
Download the url to dropbox.
"""

import urllib
import requests

url = "http://podcast-mp3.dradio.de/podcast/2016/03/07/dlf_20160307_1949_c03fc129.mp3"
path = "/home/kame/Dropbox/new_podcasts/"
urllib.request.urlretrieve(url, path + str(url[-30:]))
