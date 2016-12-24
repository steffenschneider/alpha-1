filename = "/home"
path = "/home"
line1 = "abc"
newfile = "/home"
oldfile = "/home"

# write()  # clear file in the beginning
target = open(filename, 'w')
target.write(line1)

# append
with open(path, "a") as myfile:
    myfile.write(line1)

# read()

# readline()

# readlines()

# other
with open(newfile, 'w') as outfile:
    with open(oldfile, 'r', encoding='utf-8') as infile:
        a = 1
