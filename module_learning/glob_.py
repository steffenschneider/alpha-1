# The glob module finds all the pathnames matching a specified pattern
# according to the rules used by the Unix shell

import glob

## glob
path = glob.glob("/home/kame/lex2/*.txt", recursive=False)
for filename in path:
    pass

## iglob
# Return an iterator which yields the same values as glob()
# without actually storing them all simultaneously
path2 = r"C:\Users\steffen.schneider\Desktop\RMS\**"
for filename2 in glob.iglob(path2, recursive=True):
    pass
