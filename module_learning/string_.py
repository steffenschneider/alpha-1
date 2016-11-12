## count
mystring = "alökajsdfadhfausodf"
mystring.count('a')

## Sonderzeichen to lower
#         "!§$%&/()=?`*'ÄÜÖ_:;><,.#äö+ü´ß".lower()
# output: "!§$%&/()=?`*'äüö_:;><,.#äö+ü´ß"

# ß to upper
'ß'.upper()  # 'SS'
'SS'.lower()  # 'ss'

## format
# print columns in a pretty style
# fill up points until position 40
print('{:.<40} {}'.format('aaa', 'bbb'))
