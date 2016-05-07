import re

inputtext = "http://cdn-storage.br.de/MUJIuUOVBwQIbtChb6OHu7ODifWH_-b6/_-OS/_2rH_-xf/160504_0905_radioWissen_Buddhas-Toechter---Frauen-auf-dem-Weg-zur-E.mp3"

a = re.findall("(http.*mp3)", inputtext)
print(a)
