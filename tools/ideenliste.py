# coding=utf-8

lst = [
    'Abdeckung', 'Abenteuer', 'Abfluss', 'Abwaschen', 'Akku', 'Alarm', 'Aluminiumfolie', 'Ameisenbau',
    'Analyse', 'anregen', 'Antenne', 'App (fuers Handy)', 'Aquaedukt', 'Aquarium', 'Aquedukt', 'Arduino',
    'Arztbesuch', 'Astgabelung', 'Aufkleber', 'Aufprall', 'Ausflug', 'Ausrichtung', 'Automat', 'Automatik',
    'Baby', 'Badewanne', 'Bahn', 'Bakterien', 'Bambus', 'Barcode', 'Batterie', 'Baukloetze', 'Baum', 'Baumhaus',
    'Baumrinde', 'Bausteine', 'Beamer', 'Behinderung', 'Belastung', 'Beleuchtung', 'Beschaedigung',
    'Bestellung', 'Beton', 'Bett', 'Bewaesserung', 'Bewegungssensor', 'Bienenwabe', 'Birnenform',
    'Blase', 'Blech', 'Blinker', 'Blitz', 'Blumen gießen', 'Blut', 'Bogen', 'bohren', 'Brezelform', 'Briefkasten',
    'Buechse', 'Buerste', 'Chip', 'Coach', 'Computer', 'Computerspiel', 'Dachrinne', 'Daempfung', 'Deckel',
    'Detektor', 'Diamant', 'Diebstahlsicherung', 'Diode', 'Draht', 'Drahtgeflecht', 'Dreck', 'Drohne',
    'Druck', 'duenne_Schicht', 'durchdringen', 'Durchsichtigkeit', 'Dusche', 'Ebene', 'EC-Karten-Format',
    'Ei', 'Eimer', 'Einhuellende', 'Einstein', 'Eis', 'Eisen', 'elektrischer_Summer', 'Elektromagnetismus',
    'EMV', 'Ersatz', 'Erste Hilfe', 'Erziehung', 'Escher', 'Facebook', 'Faden', 'Fahrrad', 'Fahrt_zur_Arbeit',
    'Fallschirm', 'Farben', 'Fass', 'Feder', 'Fenster', 'Fernglas', 'Fernsteuerung', 'Feuchtigkeit',
    'Feuer', 'Feuerzeug', 'Fingerabdruck', 'Flasche', 'Fliegen', 'Fluoreszenz', 'Fluss', 'Foerderband',
    'Fossilien', 'Foto', 'Fotoalbum', 'Fouriertransformation', 'Frequenzgenerator', 'Funk', 'Gabel',
    'Gabelstapler', 'Garage', 'Gegenstueck', 'Gegenteil', 'Geheimschrift', 'Geheimsignatur',
    'Geheimtuer', 'Geldschein', 'Gelenk', 'Geschwindigkeit', 'Getraenk', 'Gewicht', 'Giesskanne',
    'Gitter', 'Glas', 'Glasfaser', 'Gleichgewicht', 'Glocke', 'Glueck', 'Gold', 'GPS', 'Griff', 'Guertel',
    'Gummi', 'Gummischleuder', 'Haar', 'Haken', 'Handy', 'Haustier', 'Hebel', 'Heilkraeuter', 'Heizung',
    'Helligkeit', 'Helligkeitssensor', 'Henkel', 'Herzschrittmacher', 'Hochseilgarten', 'Hoehe',
    'Hoehle', 'Hoergeraet', 'hohl', 'Holz', 'Huelle', 'Hupe', 'Höhle', 'Igel', 'Induktion', 'Information',
    'Infrarot', 'Inneres eines Baumes', 'Insel', 'Instrument', 'Internet', 'Isolierung', 'Kabel',
    'Kabelbinder', 'Kaefer', 'Kaenguruhbeutel', 'Kaktus', 'Kaleidoskop', 'Kandis', 'Kanone', 'Kante',
    'Kapsel', 'kaputt', 'Karabinerhaken', 'Kaskade', 'Katze', 'Kaugummi', 'Kennzeichnung', 'Kerze',
    'Kette', 'Kinder', 'Kissen', 'Kiste', 'Klebeband', 'Klebstoff', 'Kleidung', 'Klettergurt', 'Klettverschluss',
    'Klingel', 'Knackfolie', 'Knoten', 'Kochen', 'Kombination', 'Kommunikation', 'Kompass', 'Komposthaufen',
    'Kondensator', 'Koordinaten', 'Kran', 'Kreis', 'Kreisel', 'Kristall', 'Kuehlung', 'Kugel', 'Kupfer',
    'Kurve', 'Körner', 'Laerm', 'Lakritz', 'Lampe', 'Laser', 'Lautsprecher', 'Lavalampe', 'LCD-Bildschirm',
    'LED', 'Lego', 'Lehm', 'Leiter', 'Licht', 'Lichtsensor', 'Lieferservice', 'Lineal', 'Linse', 'Loch',
    'Loeffel', 'Lotterie', 'Luefter', 'Luft', 'Luftballon', 'Luftfeuchtesensor', 'Luke', 'Lupe', 'Löffel',
    'Maehdrescher', 'Magnet', 'Maske', 'Massage', 'mechanische_Feder', 'Meditation', 'Medizintechnik',
    'Mehrzahl', 'Messer', 'Mikrocontroller', 'Mikrofon', 'Mikroskop', 'Mixer', 'Mond', 'Moos', 'Mosaik',
    'Motor', 'Muedigkeit', 'Muell', 'Muenze', 'Munkelbaum', 'Murmel', 'Muschel', 'Musik', 'Musikinstrument',
    'Muster', 'Nachrichten', 'Nacht', 'Nadel', 'Nagel', 'Nebel', 'Neigung', 'Netz', 'Nummer', 'Oel', 'Oelpest',
    'Papier', 'Papp-Karton', 'Pappe', 'Peltier-Element', 'Pendel', 'Periskop', 'Perle', 'Pfeife', 'Pflanze',
    'Pflaster', 'Piezo-Sensor', 'Pinzette', 'Pizza', 'Plastik', 'Polarisator', 'Prisma', 'Programm',
    'Pulver', 'Pyramdidenform', 'Pyramide', 'Quadrat', 'Quelle', 'Rad', 'Radar', 'Radioaktivitaet',
    'Rakete', 'Rasierklinge', 'Rassierklinge', 'Rauschen', 'Reflexion', 'Regen', 'Regenbogen', 'Regenwald',
    'Regenwurm', 'reiben', 'Reibung', 'Reinheit', 'Reinigung', 'Reise', 'Relativitaet', 'Religion',
    'Roboter', 'Rohrpost', 'Rolle', 'Rollen', 'Roller', 'Rutsche', 'Saege', 'Saftpresse', 'Salz', 'Sand',
    'Sandburg', 'Sanduhr', 'Scanner', 'Schachbrett', 'Schafsherde', 'Schall', 'Schalter', 'Schanze',
    'Scharnier', 'Schaukel', 'Scheibenwischer', 'Schild', 'Schlaf', 'Schlange', 'Schlauch', 'Schleuse',
    'Schloss', 'Schluessel', 'Schnecke', 'Schnee', 'Schnur', 'Schraube', 'schreddern', 'Schreiben',
    'Schrittmotor', 'Schubkarre', 'Schuhe', 'Schutthexe', 'Schutz', 'Schweben', 'schweben', 'Schwerkraft',
    'Schwingung', 'Schwingungssensor', 'sehr gross', 'sehr klein', 'sehr laut', 'sehr leise',
    'sehr_gross', 'sehr_klein', 'Seide', 'Seife', 'Seifenblase', 'Seifenkiste', 'Seil', 'Seilbahn',
    'Seilwinde', 'Sensor', 'Signal', 'Signalverabeitung', 'Silber', 'Simulation', 'Sinne', 'Sitzgelegenheit',
    'Smartphone', 'Snack', 'Solarzelle', 'Sollbruchstelle', 'Sonne', 'Spaetkauf', 'Spannung', 'spazieren_gehen',
    'Spektroskopie', 'Spiegel', 'Spiel', 'Spielzeug', 'spiralfoermig', 'Sprengstoff', 'Springbrunnen',
    'Spritze', 'Spule', 'Stadtplan', 'Stapeln', 'Staub', 'Stechbeitel', 'Stecker', 'Stern', 'sternfoermig',
    'Steuerung', 'Stoepsel', 'Strasse', 'Streichholz', 'Streit', 'Strickleiter', 'Strickmuster',
    'Stroboskob', 'Strom', 'Stromgenerator', 'Stromstaerke', 'Stöpsel', 'Suessigkeiten', 'Summer',
    'Systematik', 'sägen', 'Tafelfarbe', 'Tagging', 'Tamagochi', 'Taschenmesser', 'Tastatur', 'Taste',
    'Taster', 'Tattoo', 'Tauchen', 'Teich', 'Teilen', 'Teleskop', 'Temperatur', 'Termin', 'Theremin',
    'Tier', 'Tinte', 'Toilette', 'Ton', 'Touchscreen', 'Transformation', 'Transport', 'Trapez', 'Treppe',
    'Tresor', 'Triggerung', 'Trocknung', 'Tropf', 'Tropfen', 'Tuer', 'Tuerspion', 'Tunnel', 'Turm', 'Twitter',
    'Uhr', 'Unterkiefer', 'Urlaub', 'Vektor', 'Verband', 'Vergleich', 'Verkehr', 'Verlaengerung', 'Verschluesselung',
    'Verschmutzung', 'Verstaerker', 'Verstaerkung', 'Versteck', 'Videokamera', 'Vogelfeder',
    'Vorleseprogramm', 'Waage', 'Wandel', 'Waschsalon', 'Wasser', 'Wasserrad', 'Wassertropfen',
    'Wecker', 'Welle', 'Weltall', 'Werbung', 'Werfen', 'Werkzeug', 'Widerstand', 'Wind', 'Windmuehle',
    'Windrad', 'Winkelmesser', 'Wippe', 'Wirbel', 'WLAN', 'Wochenende', 'Wundverband', 'Zahn', 'Zahnrad',
    'Zahnreinigung', 'Zaun', 'Zeit', 'Zeitlupe', 'Zeitung', 'Zelle', 'Zen', 'Ziehen', 'Ziffer', 'Zitteraal',
    'Zucker', 'Zufall', 'Zug', 'zunehmender-Verfall', 'Zusammenfuegen', 'Uebersetzung', 'Kinder', 'Behinderte',
    'Schwangere', 'Light-Version', 'Premium-Version', 'Langeweile', 'Grenze', 'Heißluftballon', 'Prisma', 'Wolke',
    'Laerm', 'Noice-canceling', 'Pendeln', 'Konsens', 'Gehirn', 'Sport', 'Langeweile', 'Kickstarter'
]


def remove_doppelgaenger(lst_a):
    lst_b = list(set(lst_a))
    print(str(len(lst_a) - len(lst_b)) + " words removed")
    print(str(len(lst_b)) + " words in list")
    return lst_b


def sort(lst_a):
    lst_b = sorted(lst_a)
    return lst_b


def sort_case_insensitive(lst_a):
    lst_b = sorted(lst_a, key=lambda x: x.lower())
    return lst_b


def line_break_in_list(lst_a):
    size = 0
    buffer_string = "    "
    print("lst = [")
    for elem in lst_a:
        size += len(elem) + 1
        buffer_string += "'" + elem + "'"
        # don't print comma at the last item
        if elem == lst_a[len(lst_a) - 1]:
            pass
        else:
            buffer_string += ","
        buffer_string += " "
        if size > 70:
            print(buffer_string)
            buffer_string = "    "
            size = 0
    print(buffer_string)  # print last line which is maybe not so long
    print("]")


a = remove_doppelgaenger(lst)
b = sort_case_insensitive(a)
line_break_in_list(b)
