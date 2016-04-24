
import requests
import re

def run(url):

    # example link
    # url = 'http://www.heise.de/'

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

    # search for "a href"
    items = re.findall("<a href=\"(.+\.html)\"", content_)  # get links with ending .html

    # delete duplicates
    lst = list(set(list(items)))

    # return links
    for i in range(len(lst)):
        if lst[i][:4] != 'http':
            lst[i] = url + str(lst[i][1:])

    return lst

if __name__ == "__main__":
    import sys
    run(sys.argv[1])
