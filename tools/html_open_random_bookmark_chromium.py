import random
import re
import webbrowser

# open a random bookmark of my chrome bookmarks
# path to bookmarks:
file_ = "/home/kame/.config/chromium/Default/Bookmarks"

# count bookmarks
# file with lines like:            "url": "file:///home/kame/Dropbox/data/links.html"
file_input = open(file_, "r")
text = file_input.readlines()  # .read() read only one line
count = 0
for line in text:
    if '"url":' in line:
        count += 1

print(str(count) + " bookmarks available")

# choose random bookmark
rnd = random.randint(0, count)
count = 0
for line in text:
    if '"url":' in line:
        if count == rnd:
            line_with_link = line
        count += 1

# extract link
url = re.findall(r"url.*\"(.*)\"", line_with_link)[0]
print(url)

# open in chrome browser
webbrowser.open(url, new=2)  # open in a new tab, if possible
