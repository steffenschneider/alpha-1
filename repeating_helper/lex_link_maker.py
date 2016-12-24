# coding=utf-8
import os


def main():
    # get content
    if os.name == 'posix':
        pathes = ["/home/kame/Dropbox/main-lex.txt",
                  # "/home/kame/Dropbox/main-lex-work.txt",  # schlecht wegen Programmcode
                  "/home/kame/Desktop/main/diary.txt",
                  ]
    elif os.name == 'nt':
        pathes = ["C:/Users/steffen.schneider/dropbox/main-lex.txt",
                  # "C:/Users/steffen.schneider/dropbox/main-lex-work.txt",  # schlecht wegen Programmcode
                  # "C:/Users/steffen.schneider/dropbox/diary.txt",  # not available
                  ]

    for path in pathes:
        # print("Searching duplicates in file --> " + str(path))
        with open(path, "r", encoding='utf8') as infile:
            text = infile.readlines()  # .read() read only one line

        new_text = []

        # find article name and save to list
        list_with_article_words = []
        for line in text:
            if line[:2] == '##':
                list_with_article_words.append(line[2:-1])  # OK

        # replace words
        with open(path, 'w', encoding='utf8') as outfile:
            for sentence in text:
                for word in sentence.split(' '):
                    # print(word)
                    search_word = word.strip("\n")
                    search_word2 = search_word.strip(",")
                    search_word3 = search_word2.strip(".")
                    search_word4 = search_word3.strip(")")
                    search_word5 = search_word4.strip("(")
                    search_word6 = search_word5.strip("-")
                    search_word7 = search_word6.strip(";")
                    search_word8 = search_word7.strip(":")
                    search_word9 = search_word8.strip("!")

                    # print("search_word: " + str(search_word5))
                    if search_word9 in list_with_article_words:
                        print(word)
                        if "\n" in word:
                            word = "░" + str(word[:-1]) + "░" + "\n"
                        else:
                            word = "░" + str(word) + "░"
                    outfile.write(word)
                    if "\n" in word:
                        pass
                    else:
                        outfile.write(" ")


if __name__ == '__main__':
    main()
