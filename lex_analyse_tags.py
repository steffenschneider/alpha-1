# coding=utf-8

"""
Remove irrelevant tags from my main-lex.txt file.
Show the use of new tags.
"""


def run():
    import re
    print("+++ lex_analyse_tags.py called +++")

    # open file
    path = "/home/kame/Dropbox/"
    filename = "main-lex.txt"
    file_ = path + filename

    taglist = ['!', '!!', '!!!', 'A', 'Abkürzung', 'Algebra', 'Arbeit', 'Astronomie',
               'Auto', 'awk', 'Bash', 'Biologie', 'Botanik',
               'Buch', 'C', 'Chemie', 'Computer', 'Cpp', 'Datenbank', 'Elektrotechnik', 'Erfindung',
               'Ernährung', 'Gehirn', 'Genetik', 'Geographie',
               'Geologie', 'Geschichte', 'git', 'GPS', 'Hardware', 'Hochfrequenztechnik', 'HTML', 'Japan',
               'Java', 'JavaScript', 'Jenkins', 'jQuery', 'KI', 'Kochen', 'Kommunikation', 'Lasertechnik',
               'Latex', 'Linux', 'Materialwissenschaften', 'Mathematik', 'Matlab',
               'Mechanik', 'Medizin', 'Messtechnik', 'Mikrocontroller',
               'MRT', 'Nico', 'Optik', 'Organisation', 'Persönlichkeit', 'Philosophie', 'PHP', 'Physik', 'Physiologie',
               'Politik', 'Programmieren', 'Programmieren-Vorgehensmodell',
               'Psychologie', 'Python', 'Quantenphysik', 'Raumfahrt',
               'Radar', 'Rechtschreibung', 'Regex', 'Rest', 'Robot',
               'Security', 'Selenium', 'Signalverarbeitung',
               'Software', 'Soziologie', 'SQL', 'Strahlenphysik', 'svn', 'Technik', 'Testing',
               'Testprogramm', 'Tier', 'todo', 'Umweltschutz', 'VB', 'Verweis',
               'Windows', 'Wirtschaft', 'Wortschatz', 'WPF', 'XAML', 'XML', 'XNA', 'Zen']

    # key: used tag
    # value: tag you should use instead
    replacement_dict = {'Astrophysik': 'Astronomie',
                        'Falschschreibung': 'Rechtschreibung',
                        'Garten': 'Botanik',
                        'Lesen': 'Buch',
                        'Mineral': 'Geologie',
                        'Modbus': 'Elektrotechnik',
                        'Netzwerktechnik': 'Computer',
                        'Programming': 'Programmieren',
                        'PyCharm': 'Software',
                        'Pyhton': 'Python',
                        'Radio': 'Rest',
                        'Recht': 'Rest',
                        'regex': 'Regex',
                        'RMS': 'Testprogramm',
                        'Stochastik': 'Mathematik'
                        }

    with open(file_) as f:
        content = f.readlines()

    found_empty = 0

    for i in range(len(content)):
        # print(content[i])

        if content[i] == "\n":
            found_empty = 1
        if found_empty > 0:
            found_empty += 1

        # get tags two lines behind an empty line
        if found_empty == 4:
            if re.search(r"\[.{0,40}\]", content[i]):
                found_empty = 0
                mo = re.search(r"\[.{0,40}\]", content[i])
                if mo.group()[1:-1] in taglist:
                    pass
                elif mo.group()[1:-1] in replacement_dict:
                    # show obsolete tags
                    key = mo.group()[1:-1]
                    print(key),
                    # change tag to the following tag
                    print(" --> "),
                    print(replacement_dict[key])
                else:
                    # show new tags
                    print("New tag found: " + str(mo.group()[1:-1]))


if __name__ == '__main__':
    run()
