"""
Get news from news-websites.
Work in progress!!!
"""

import re

import requests


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

    # xpath of useful content
    # //*[@id="mitte_news"]/article/div/p[1]/strong/text()
    # //*[@id="mitte_news"]/article/div/p[2]
    # //*[@id="mitte_news"]/article/div/p[1]/strong

    # search for "a href"
    # content_ = re.sub('</?a.+>', '', content_)
    # content_ = re.sub('</font.+>', '', content_)
    # content_ = re.sub('<span.+>', '', content_)
    # content_ = re.sub('</span>', '', content_)
    # content_ = re.sub('</?strong>', '', content_)
    # content_ = re.sub('<br.+>', '', content_)
    # content_ = re.sub('</?em>', '', content_)
    # content_ = re.sub('</?b>', '', content_)
    # content_ = re.sub('</?li.*>', '', content_)
    # content_ = re.sub('</?html.*>', '', content_)
    # content_ = re.sub('</?body.*>', '', content_)
    # content_ = re.sub('</?ul.*>', '', content_)
    # content_ = re.sub('</?script.*>.*<.+>', '', content_)
    # content_ = re.sub('</?script>', '', content_)
    # content_ = re.sub('</?head>', '', content_)
    # content_ = re.sub('</?div>', '', content_)
    # content_ = re.sub('</?title>', '', content_)
    # content_ = re.sub('<meta.+/?>', '', content_)
    # content_ = re.sub('<!--.*-->', '', content_)

    # items = re.findall("<p>(.+)</p>", content_)  # get text within <p></p>
    # // *[ @ id = "mitte_news"] / article / div / p[1]
    items = re.findall("<p>(.+)</p>", content_)  # get text within <p></p>
    # items = content_

    # return content
    # todo
    return items


if __name__ == "__main__":
    import sys

    run(sys.argv[1])
