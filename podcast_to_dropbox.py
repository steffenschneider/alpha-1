# coding=utf-8

"""
Download all new podcast episodes to /Dropbox/new_podcasts.
Before delete the old files in this folder.   todo
"""

# todo
# check newest file
# only download newer files
# if no file --> download all


def get_podcasts():
    # print(sys.version_info)
    import collections
    import mydata
    import requests
    import re
    import f
    import urllib.request
    # retrieve podcast data
    podcast_links_dict = mydata.podcast_links_dict

    # sort dict
    podcast_links_dict_ordered = collections.OrderedDict(sorted(podcast_links_dict.items()))

    # for every podcast in my list
    for i in range(len(podcast_links_dict_ordered)):
        url = list(podcast_links_dict_ordered.values())[i]
        try:
            response = requests.get(url)
            content_binary = response.content
            content_ = content_binary.decode('utf-8')

            # find mp3 link
            if 'deutschlandfunk' in url:
                items = re.findall("<guid>(http://.+_.+\.mp3)", content_)

                # print first mp3-url
                print(items[0].split('\"')[0])
                mp3_url = items[0].split('\"')[0]
                # mp3_url = "http://podcast-mp3.dradio.de/podcast/2016/03/12/dlf_20160312_1630_83264bea.mp3"
                path = "/home/kame/Dropbox/new_podcasts/"
                filetype = ".mp3"

                # download file if not downloaded yet
                podcastlist = f.get_filenames_from_dir(path)
                found = 0
                for j in range(len(podcastlist)):
                    if str(mp3_url[-26:-13]) in podcastlist[j]:
                        # print("File downloaded before")
                        found = 1  # file already downloaded
                if found == 0:  # if not yet downloaded
                    print("File number " + str(i + 1) + " will be downloaded now.")
                    podcast_name = list(podcast_links_dict_ordered.keys())[i]
                    date_ = mp3_url[-26:-13]
                    place = str(path) + str(date_) + ' ' + str(podcast_name) + filetype
                    url_ = str(mp3_url)
                    # print(url_)
                    urllib.request.urlretrieve(url_, place)

            if 'br-online' in url:
                urls = re.findall("(http.*mp3)", content_)
                titles = re.findall("[\d].*/(.*mp3)", content_)

                # print first mp3-url
                print(333)
                mp3_url = urls[2]  # the third element is the first mp3
                print(mp3_url)
                path = "/home/kame/Dropbox/new_podcasts/"

                print(555)
                # download file if not downloaded yet
                podcastlist = f.get_filenames_from_dir(path)
                found = 0
                print(666)
                for j in range(len(podcastlist)):
                    if str(mp3_url) in podcastlist[j]:
                        # print("File downloaded before")
                        found = 1  # file already downloaded
                print(888)
                if found == 0:  # if not yet downloaded
                    print(999)
                    print("File number " + str(i + 1) + " will be downloaded now.")
                    place = str(path) + str(titles[2])
                    urllib.request.urlretrieve(mp3_url, place)

        except:
            print("Exception: Could not download the file!!!!!!!!!!!!!!!!!!")
            break

    # http://www1.swr.de/podcast/xml/swr2/wissen.xml
    # http://www.br-online.de/podcast/mp3-download/bayern2/mp3-download-podcast-radiowissen.shtml

if __name__ == "__main__":
    get_podcasts()
