import f
from f import Pathes

def main():
    # get content
    pathes = [Pathes.main_lex_work,
              Pathes.main_lex,
              Pathes.diary
              ]

    for path in pathes:
        f.file_replace_words(path, 'garnicht', 'gar nicht')
        f.file_replace_words(path, 'daselbe', 'dasselbe')
        f.file_replace_words(path, 'Addresse', 'Adresse')
        f.file_replace_words(path, 'geschaft', 'geschafft')
        f.file_replace_words(path, 'javascript', 'JavaScript')
        f.file_replace_words(path, 'werdne', 'werden')
        f.file_replace_words(path, 'Pyhton', 'Python')
        f.file_replace_words(path, 'Fuss', 'Fuß')

if __name__ == '__main__':
    main()
