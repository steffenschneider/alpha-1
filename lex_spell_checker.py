# get content
pathes = ["/home/kame/Dropbox/main-lex.txt",
          "/home/kame/Dropbox/main-lex-arbeit.txt",
          "/home/kame/Dropbox/diary.txt"
          ]

for path in pathes:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(path)
    file_input = open(path, "r")
    text = file_input.readlines()  # .read() read only one line

    lst_wrong = ['garnicht', 'Pyhton', 'daselbe', 'werdne']

    for item in lst_wrong:
        for line in text:
            if item in line:
                print(item, line)
