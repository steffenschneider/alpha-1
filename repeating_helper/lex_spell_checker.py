def main():
    # get content
    pathes = ["/home/kame/Dropbox/main-lex.txt",
              "/home/kame/Dropbox/main-lex-work.txt",
              "/home/kame/Desktop/diary.txt"
              ]

    for path in pathes:
        file_input = open(path, "r")
        text = file_input.readlines()  # .read() read only one line

        lst_wrong = ['garnicht', 'Pyhton', 'daselbe', 'werdne', 'Addresse']

        for item in lst_wrong:
            for line in text:
                if item in line:
                    print(item, line)


if __name__ == '__main__':
    main()
