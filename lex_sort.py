# -*- coding: utf-8 -*-

# works also in csharp
# if 'posix' in os.name:
#    os.system("wine /home/kame/Dropbox/code/csharp/monodevelop/lex_/lex_/bin/Debug/lex_.exe")
# if 'nt' in os.name:
#    print("Doesn't work under windows because of wrong path in csharp file.")
#    os.system("C:/Users/kame/Dropbox/code/csharp/monodevelop/lex_/lex_/bin/Debug/lex_.exe")


def main():
    # get content
    pathes = ["/home/kame/Dropbox/main-lex.txt",
              "/home/kame/Dropbox/diary.txt"
              ]

    for path in pathes:
        print(path)
        file_input = open(path, "r")
        text = file_input.readlines()  # .read() read only one line

        # create 2d-list
        lst = []
        row = -1
        column = 0
        n_articles = 0
        for line in text:
            if line[:2] == '##':
                n_articles += 1

        print("number of articles: " + str(n_articles))

        for i in range(n_articles):
            lst.append([])

        # every article goes in one list-row
        for line in text:
            if line[:2] == '##':  # new article
                column = 0
                row += 1
            lst[row].append(line)

        # todo - eventuell loeschen
        for i in range(n_articles):
            try:
                if lst[i][0] == '\n':  # or lst[i][0] == '':
                    lst[i].append('')
            except:
                lst[i].append('')  # important for sorting; cell must not be empty
                lst[i].append('')

        # sort articles - first tag - then name
        outputlst = sorted(lst, key=lambda x: (x[1].lower(), x[0].lower()))

        # write new file
        f = open(path, 'w')
        for i in range(n_articles):
            for j in range(len(outputlst[i])):
                f.write(outputlst[i][j])


if __name__ == '__main__':
    main()
