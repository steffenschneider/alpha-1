import random
import time
import webbrowser

# list with funny search words
lst = ["asi", "siw", "star wars 4", "henne oder ei", "verdorbene milch", "kss"
                                                                         "iq unter 80 kein problem?", "managerseminar",
       "spww", "söxn",
       "ich verdiene zu viel", "ständig ruft jemand an",
       "beate meier", "hans breitscheid", "sven steffen",
       "deutscher meister handball", "schlüssel verloren",
       "audi a7 kühlung defekt", "smartphone günstig",
       "pokemon go", "bin ich zu blond?", "schlüssel nachmachen",
       "selbstbeteiligung", "hauskauf gütersloh", "gütersloh immobilien",
       "sommersonnenwände", "wie bekomme ich meine falten weg",
       "betrug glöcksspiel", "wie geht waschmaschine an siemens 2810",
       "Glaubt ihr auch an Gott", "mir ist immer langweilig",
       "jupiter", "andromedar", "auto kaufen", "bmw", "audi",
       "kühlschrank reparieren", "wie finde ich eine freundin",
       "hgd"]

for i in range(22):
    rnd = random.choice(lst)
    url = 'https://www.google.de/search?q=' + str(rnd)
    webbrowser.open(url, new=0)  # open in a new tab, if possible
    rnd2 = random.randint(0, 30)
    time.sleep(10 + rnd2)

    # todo
    # get other words for list
    # close tab after visiting?
    # run in background

    # click first link?
