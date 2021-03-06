# coding=utf-8

#  csharp script also works
# os.system("wine /home/kame/Dropbox/code/csharp/monodevelop/lex-duplicates/" +
#  "lex-duplicates/bin/Debug/lex-duplicates.exe")


def main():
    import os
    # get content
    if os.name == "posix":
        pathes = ["/home/kame/Dropbox/main-lex.txt",
                  "/home/kame/Dropbox/main-lex-work.txt",
                  "/home/kame/Desktop/main/diary.txt"
                  ]
    elif os.name == "nt":
        pathes = ["C:/Users/steffen.schneider/dropbox/main-lex.txt",
                  "C:/Users/steffen.schneider/dropbox/main-lex-work.txt",
                  ]


    for path in pathes:
        # print("Searching duplicates in file --> " + str(path))
        file_input = open(path, "r", encoding='utf8')
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
        lst_duplicates = sorted(lst_duplicates)

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
                print("Duplicate found in --> " + str(path) + "   Element --> " + str(elem))
            lst_tags = []


if __name__ == '__main__':
    main()
