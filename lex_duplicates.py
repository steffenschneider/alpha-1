# csharp script also works
# os.system("wine /home/kame/Dropbox/code/csharp/monodevelop/lex-duplicates/lex-duplicates/bin/Debug/lex-duplicates.exe")

# get content
pathes = ["/home/kame/Dropbox/main-lex.txt",
          "/home/kame/Desktop/diary.txt"
          ]

for path in pathes:
    print("Searching duplicates in file --> " + str(path))
    file_input = open(path, "r")
    text = file_input.readlines()  # .read() read only one line

    # find article name duplicates and save to list
    lst = []
    for line in text:
        if line[:2] == '##':
            lst.append(line)

    from collections import Counter

    lst_duplicates = []
    c = Counter(lst)
    for letter, count in c.most_common(1111):
        if count > 1:
            lst_duplicates.append(letter)
    lst_duplicates = list(set(lst_duplicates))
    # print(sorted(lst_duplicates))

    # look at tags of each duplicate
    lst_tags = []
    for elem in lst_duplicates:
        found = 0
        for line in text:
            if found == 1:
                lst_tags.append(line)
                found = 0
            if line == elem:
                # print(elem)
                found = 1
        # print(lst_tags)
        if len(lst_tags) != len(list(set(lst_tags))):
            print("Duplicate found.")
            print(elem, lst_tags)
        lst_tags = []
