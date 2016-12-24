# coding=utf-8

# works also in csharp
# if 'posix' in os.name:
#    os.system("wine /home/kame/Dropbox/code/csharp/monodevelop/lex_/lex_/bin/Debug/lex_.exe")
# if 'nt' in os.name:
#    print("Doesn't work under windows because of wrong path in csharp file.")
#    os.system("C:/Users/kame/Dropbox/code/csharp/monodevelop/lex_/lex_/bin/Debug/lex_.exe")

import os

def main():
    # get content
    if os.name == 'nt':  # Windows
        pathes = [  # "C:/Users/steffen.schneider/Dropbox/main-lex.txt",
            "C:/Users/steffen.schneider/Dropbox/main-lex-work.txt",
            # "C:/Users/steffen.schneider/Desktop/main/diary.txt",
        ]
    elif os.name == 'posix':
        pathes = ["/home/kame/Dropbox/main-lex.txt",
                  "/home/kame/Dropbox/main-lex-work.txt",
                  "/home/kame/Desktop/main/diary.txt",
                  ]
    else:
        raise Exception("unknown system")

    for path in pathes:
        # print(path)
        file_input = open(path, "r", encoding='utf-8')
        text = file_input.readlines()  # .read() read only one line

        # create 2d-list
        lst = []
        row = -1
        n_articles = 0
        for line in text:
            if line[:2] == '##':
                n_articles += 1

        # print("number of articles: " + str(n_articles))

        for i in range(n_articles):
            lst.append([])

        # every article goes in one list-row
        for line in text:
            if line[:2] == '##':  # new article
                row += 1
            lst[row].append(line)

        # ?
        for j in range(n_articles):
            try:
                if lst[j][0] == '\n':  # or lst[j][0] == '':
                    lst[j].append('')
            except ValueError:
                lst[j].append('')  # important for sorting; cell must not be empty
                lst[j].append('')

        # check list-entry-format
        for k in range(n_articles):
            # article name should start with two hash-signs
            error_message_1 = "Article: " + str(lst[k][0])
            assert lst[k][0][:2] == '##', error_message_1
            # tag should stay in square brackets
            try:
                error_message_2 = "Tag: " + str(lst[k][1])
            except:
                print(k)
                print(lst[k][0])
            assert lst[k][1][0] == '[', str(error_message_1) + "  " + str(error_message_2)
            assert lst[k][1][-2] == ']', lst[k][0]

        # sort articles - first tag - then name
        outputlst = sorted(lst, key=lambda x: (x[1].lower(), x[0].lower()))

        # write new file
        f = open(path, 'w', encoding='utf-8')
        for i in range(n_articles):
            for j in range(len(outputlst[i])):
                f.write(outputlst[i][j])

if __name__ == '__main__':
    main()
