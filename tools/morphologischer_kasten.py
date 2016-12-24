import random

##tisch
lst_tisch = [
    ['Form:', 'Ein ', '', 'eiförmiger', 'elliptischer', 'runder', 'runder', 'quadratischer', 'dreieckiger'],
    ['Größe:', '', '', 'kleiner', 'großer', 'mittelgroßer'],
    ['Farbe:', '', '', 'roter', 'blauer', 'grüner', 'brauner', 'gelber', 'weißer', 'schwarzer', 'pinkfarbener',
     'bunter', 'farbloser'],
    ['Material:', '', 'tisch', 'Holz', 'Holz', 'Stein', 'Metall', 'Glas'],
    ['Tischbeine:', 'mit ', ' Beinen', '0', '1', '2', '3', '3', '4', '100'],
    ['Fächer:', 'und ', ' Fächer', 'mit', 'ohne'],
]

##fahrzeug
lst_lego_fahrzeug = [
    # Attribut, Präfix, Suffix, Variationen
    ['Farbe:', 'Ein ', ' Fahrzeug', 'orangenes', 'gelbes', 'blaues', 'weißes'],
    ['Räder:', 'mit ', ' Rädern ', '0', '1', '2', '3', '4', '6', '8'],
    ['Sitze:', 'mit ', ' Sitzen', '0', '1', '2', '4', '15'],
    ['Scheibe:', 'mit ', ' Scheiben', '0', '1', '3', '8'],
    ['Flügel', '', ' Flügel', 'mit', 'ohne'],

]

for item in lst_tisch:
    rnd_item = random.randint(3, len(item) - 1)
    print(item[1] + item[rnd_item] + item[2])
