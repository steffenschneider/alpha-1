# coding=utf-8

"""
Remove irrelevant tags from my main-lex.txt file.
Show the use of new tags.
"""


def main():
    import re

    # open file
    pathes = ["/home/kame/Desktop/main/diary.txt",
              "/home/kame/Dropbox/main-lex.txt",
              "/home/kame/Dropbox/main-lex-work.txt"
              ]

    for path in pathes:
        taglist = ['!', '!!', '!!!', 'A', 'Abkürzung', 'Algebra',
                   'ajax', 'Arbeit', 'Astronomie',
                   'Auto', 'awk', 'Bash', 'Biologie', 'Botanik',
                   'Buch', 'C', 'Chemie', 'Computer', 'Cpp', 'CSharp',
                   'CSS', 'Datenbank', 'Elektrotechnik',
                   'Erfindung',
                   'Ernährung', 'Error', 'Gehirn', 'Genetik', 'Geographie',
                   'Geologie', 'Geschichte', 'git', 'GPS', 'Hardware',
                   'Hochfrequenztechnik', 'HTML', 'Japan',
                   'Java', 'JavaScript', 'Jenkins', 'jQuery', 'KI',
                   'Kochen', 'Kommunikation', 'Lasertechnik',
                   'Latex', 'Linux', 'Literatur',
                   'Materialwissenschaften', 'Mathematik', 'Matlab',
                   'Mechanik', 'Medien', 'Medizin', 'Messtechnik', 'Mikrocontroller',
                   'MRT', 'Netzwerktechnik', 'Nico', 'Optik',
                   'Organisation', 'Persönlichkeit', 'Philosophie', 'PHP',
                   'Physik', 'Physiologie',
                   'Politik', 'privat', 'Programmieren', 'Programmieren-Vorgehensmodell',
                   'Psychologie', 'Python', 'Quantenphysik', 'r', 'Raumfahrt',
                   'Radar', 'Rechtschreibung', 'Regex', 'Religion', 'Rest', 'Robot',
                   'Security', 'Selenium', 'Signalverarbeitung',
                   'Software', 'Soziologie', 'SQL', 'Strahlenphysik',
                   'svn', 'Systemtest', 'Tagebuch', 'Technik',
                   'Testing',
                   'Testprogramm', 'Tier', 'todo', 'Umweltschutz', 'VB', 'vbnet', 'Verweis',
                   'Windows', 'Wirtschaft', 'Wissen', 'Wortschatz',
                   'WPF', 'XAML', 'XML', 'XNA', 'Zen',
                   'Elektrotechnik][Modbus',
                   'r][devices', 'r][Systemtest', 'r][Webtest', 'r][Webtest][robot',
                   ]

        # key: used tag
        # value: tag you should use instead
        replacement_dict = {'Astrophysik': 'Astronomie',
                            'Falschschreibung': 'Rechtschreibung',
                            'Garten': 'Botanik',
                            'Lesen': 'Buch',
                            'Mineral': 'Geologie',
                            'Modbus': 'Elektrotechnik',
                            'Programming': 'Programmieren',
                            'PyCharm': 'Software',
                            'Pyhton': 'Python',
                            'Radio': 'Rest',
                            'Recht': 'Rest',
                            'regex': 'Regex',
                            'RMS': 'Testprogramm',
                            'Stochastik': 'Mathematik',
                            'Umwelt': 'Umweltschutz',
                            'rms': 'r'
                            }

        with open(path) as f:
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
                if re.search(r"^\[.{0,40}\]", content[i]):  # if brackets available
                    found_empty = 0
                    mo = re.search(r"\[.{0,40}\]", content[i])
                    if mo.group()[1:-1] in taglist:  # if tag in taglist
                        if mo.group()[1:-1] == "privat" and "main-lex" in path:
                            print("[privat] found in " + str(path))
                        else:
                            pass
                    elif mo.group()[1:-1] in replacement_dict:
                        # show obsolete tags
                        key = mo.group()[1:-1]
                        print(key)
                        # change tag to the following tag
                        print(" --> ")
                        print(replacement_dict[key])
                    else:
                        # show new tags
                        print("New tag found in file --> " + str(path) + " --- " + str(mo.group()[1:-1]))


if __name__ == '__main__':
    main()
