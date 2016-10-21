import re

# string = "http://cdn-storage.br.de/MUJIuUOVBwQIbtChb6OHu7ODi" \
#            "fWH_-b6/_-OS/_2rH_-xf/160504_0905_radioWissen_Budd" \
#            "has-Toechter---Frauen-auf-dem-Weg-zur-E.mp3"

string = "<title><![CDATA[Coronation Street star Jean Alexander dies aged 90]]></title>"

# if re.search(r'^[789]\d{9}$', string):
#     print("found")
# else:
#     print("not found")

result = re.findall(r"(.*)</title>", string)
print(result)

# result = re.sub(r"]]", "", string)
# print(result)


# end       $
# start     ^
# numbers   \d
