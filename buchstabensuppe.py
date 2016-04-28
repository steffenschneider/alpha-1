#!/usr/bin/env python3
# coding: utf-8

# Erzeugt eine Buchstabensuppe, in der man die Wörter suchen muss, die man
# vorher eingegeben hat.
# Author: Erik Streb del Toro
# Licence: GPL v3 or newer
# Changelog:
#   - 2015-12-10: first working version
#   - 2015-12-11: Überlappungen und Dimensionen werden angezeigt (könnte beides
#                 auch in return-Anweisung fließen, damit nur die Matrix
#                 ausgegeben wird)
#   - 2015-12-12: svg-Ausgabe
#   - 2015-12-14: doppelte Worte innerhalb der Suppenerstellungsfunktion
#   - 2015-12-22: Wortliste nach Länge sortieren, längstes zuerst,
#                 große Buchstabensuppen mit 20x20 Feldern
#   - 2015-12-23: Per Kommandozeilenparameter steuerbar,
#                 beliebiges Alphabet
#   - 2016-01-06: doc-strings, Fehlerbehandlung bei zu kleiner Suppe
#   - 2016-01-09: Fehler behoben: ß wurde zu ss,
#                 Lösungswort in die leeren Zellen
#
# FIXME:
# • bei 54 Wörtern, sind 20 nicht auf dem Blatt, also Schrift unten noch
#   kleiner machen
# • Hinweis auf Lösungswort in SVG
# TODO:
# • einlesen von ergebnis-Dateien (einheitliches Format?)
# • zeitliche abbruchbedingung einbauen
# • GUI basteln, dann können die kinder das am rechner spielen
# • bei gcompris einreichen
# • man könnte das gleiche für gcompris mit farben oder mustern/icons machen,
#   also statt buchstaben (hä, was habe ich hier gemeint? farbmuster suchen, die
#   irgendwo stehen, oh man, das hört sich schwierig an!)

import random
import sys      # um das Programm bei Fehlern zu beenden
import string   # für das Alphabet
import argparse


def wortereinlesen(maxLen):
  """
  Worte interaktiv einlesen.
  """
  WEwortliste = []
  while True:
    wort = input("Bitte wörter eingeben; oder Enter für Ende: ")
    if len(wort) > 0:
      if len(wort) <= maxLen:
        WEwortliste += [wort]
      else:
        print("Das Wort darf höchstens "+str(maxLen)+" Zeichen haben.")
    else:
      break
  return WEwortliste


def deleteSubstringsFromStringList(DSwortliste):
  """
  Lösche kurze Worte, wenn sie Teilworte von anderen Worten sind.
  """
  mengeDerWorte = list(set(DSwortliste))
  for subWort in mengeDerWorte:

    anzahlSubWorte = 0
    for wort in mengeDerWorte:
      if subWort in wort or subWort[::-1] in wort:
        anzahlSubWorte += 1
    
    if anzahlSubWorte > 1:
      mengeDerWorte.remove(subWort)

  return mengeDerWorte


def buchstabensuppe_erzeugen( BEwortliste, BEmaxX, BEmaxY,
                              BEreversed=True,
                              BEerlaubteVersuche=1000,
                              BEminDiagonale=0):
  """
  Verteile die Wörter in der Buchstabensuppe.
  """

  # erste sub-wörter entfernen
  BEwortliste = deleteSubstringsFromStringList(BEwortliste)

  # dann liste nach Länge sortieren, längstes zuerst
  BEwortliste.sort(key=len,reverse=True)

  BEanzahlWorte = len(BEwortliste)


  # X = 0     X = 1     X = 2        Richtungen: 4 Stück
  # spalte1   spalte2   spalte3                 D
  #                                           C
  # Y = 0 <=> zeile1                        B
  # Y = 1 <=> zeile2                      A
  # Y = 2 <=> zeile3                    
  #                                    0
  # matrix[Y][X]                        1 ABCD
  #                                    2
  #                                  3    
  #                                        A
  #                                  A       B
  #                                  B         C
  #                                  C           D
  #                                  D

  for BEversuch in range(BEerlaubteVersuche):
    #print(BEerlaubteVersuche-BEversuch, end=" ")
    #sys.stdout.flush()

    matrix = [["." for x in range(BEmaxX)] for x in range(BEmaxY)]

    BEausgelasseneWorte = 0
    BEanzahlUeberlappungen = 0
    BEanzahlDiagonale = 0
    for einWort in BEwortliste:
      lenEinWort = len(einWort)
      # so lange versuchen eine Position und Richtung zu finden, bis kein anderer
      # Buchstabe mehr mit einem ungleichen Buchstaben überschrieben wird
      sucheWerte = True
      anzahlVersucheMitDiesenWerten = 0
     
      while sucheWerte:
        sucheWerte = False
        anzahlVersucheMitDiesenWerten += 1
        anzahlUeberlappungenSucheWerte = 0
        # Felder, Anzahl Richtungen, vor-/rückwärts
        if anzahlVersucheMitDiesenWerten > BEmaxX*BEmaxY*4*2:
          #print("Wort "+einWort+" ausgelassen. Keinen Platz gefunden.")
          BEausgelasseneWorte += 1
          break
        if BEreversed:
          richtungVorRueck = random.choice([-1, 1])
        else:
          richtungVorRueck= 1

        if lenEinWort > BEmaxX:
          richtungNr = 3
        elif lenEinWort > BEmaxY:
          richtungNr = 1
        else:
          richtungNr = random.randrange(4)

        offsetY = 0
        if richtungNr == 0:
          richtX = 1
          richtY = -1
          lenX = lenEinWort
          lenY = lenEinWort
          offsetY = lenY - 1
        elif richtungNr == 1:
          richtX = 1
          richtY = 0
          lenX = lenEinWort
          lenY = 1
        elif richtungNr == 2:
          richtX = 1
          richtY = 1
          lenX = lenEinWort
          lenY = lenEinWort
        elif richtungNr == 3:
          richtX = 0
          richtY = 1
          lenX = 1
          lenY = lenEinWort
        else:
          print("FEHLER! »richtungNr« muss zwischen 0 und 3 liegen")
          sys.exit(3)


        startX = random.randrange(BEmaxX - lenX + 1)
        startY = random.randrange(BEmaxY - lenY + 1) + offsetY

        fertigesWort = einWort[::richtungVorRueck].replace("ß","ẞ").upper()

        # nicht gleich am Anfang schreiben, sondern erst prüfen, ob die zu
        # schreibenden Buchstaben keine anderen Buchstaben überschreiben
        schreiben = False
        for pruefenDannSchreiben in range(2):
          if sucheWerte:
            # wurde weiter unten auf True gesetzt, da es eine
            # Buchstabenkollision gab, deshalb soll auch diese
            # prüfen-schreiben-Schleife verlassen werden
            break
          for pos in range(lenEinWort):
            distX = startX+richtX*pos
            distY = startY+richtY*pos
            if distX < BEmaxX and distY < BEmaxY and distX >= 0 and distY >= 0:
              if schreiben:
                matrix[distY][distX] = fertigesWort[pos]
              else:
                # wenn da kein freies Feld mehr ist, also ein ».«, dann wird es
                # kritisch und erfordert weitere Prüfungen
                if matrix[distY][distX] != ".":
                  # prüfen ob bereits ungleicher Buchstabe vorhanden ist, wenn
                  # ja, dann neuer würfelversuch
                  if matrix[distY][distX] != fertigesWort[pos]:
                    sucheWerte = True
                    break
                  # wenn es nicht ».« ist, und auch kein anderer Buchstabe,
                  # dann muss es der gleiche Buchstabe sein
                  else:
                    anzahlUeberlappungenSucheWerte += 1
                  
            else:
              print("FEHLER! distX und distY müssen innerhalb von (0,0) "+
                  "und ("+str(BEmaxX)+","+str(BEmaxY)+") liegen")
              sys.exit(4)
          if not sucheWerte and pruefenDannSchreiben == 0:
            schreiben = True
            if richtungNr == 0 or richtungNr == 2:
              BEanzahlDiagonale += 1

      BEanzahlUeberlappungen += anzahlUeberlappungenSucheWerte

    if BEausgelasseneWorte == 0 and BEanzahlDiagonale >= BEminDiagonale:
      break

  BEversuch+=1

  return matrix, BEversuch, BEanzahlWorte, BEausgelasseneWorte, BEanzahlUeberlappungen, BEanzahlDiagonale


def buchstabensuppe_loesungswort(BLsuppe, BLloesungswort):
  """
  Fülle die leeren Zellen der Buchstabensuppe mit LÖSUNGSWORT auf.
  """

  def rand_perm(wort):
    """
    Erzeugt eine zufällige Permutation eines Wortes, also vertauscht die
    Buchstaben.
    """
    import random

    wortAlsListe = list(wort)
    neuesWort = ""

    for i in range(len(wort)):
      selectedChar = random.choice(wortAlsListe)
      wortAlsListe.remove(selectedChar)
      neuesWort += selectedChar

    print(neuesWort)

  BLleereZellen = 0

  # leere Zellen zählen
  for zeile in range(len(BLsuppe)):
    for spalte in range(len(BLsuppe[0])):
      if BLsuppe[zeile][spalte] == ".":
        BLleereZellen += 1

  if len(BLloesungswort) > BLleereZellen:
    print("FEHLER! Lösungswort", len(BLloesungswort), "ist länger als Anzahl der leeren Zellen", BLleereZellen)
    sys.exit(5) # FIXME:  Oder soll das hier nicht abbrechen, sondern weiter
                #         neue Suppen erzeugen?

  loesungswortAufgefuellt = ( list(BLloesungswort.replace("ß","ẞ").upper()
      + "."*(BLleereZellen-len(BLloesungswort))) )

  # Lösungswort schreiben
  for zeile in range(len(BLsuppe)):
    for spalte in range(len(BLsuppe[0])):
      if BLsuppe[zeile][spalte] == ".":
        selectedChar = random.choice(loesungswortAufgefuellt)
        loesungswortAufgefuellt.remove(selectedChar)
        BLsuppe[zeile][spalte] = selectedChar

  return BLsuppe


def buchstabensuppe_auffuellen(BAsuppe, nurBuchstabenDieNichtInWortenVorkommen=True, BAalphabet=string.ascii_uppercase):
  """
  Fülle die leeren Zellen der Buchstabensuppe mit Buchstaben auf.
  """
  BAleereZellen = 0
  if nurBuchstabenDieNichtInWortenVorkommen:
    fuellzeichenListe = list(set(BAalphabet.replace("ß","ẞ").upper()) -
        set("".join(["".join(BAsuppe[i]) for i in range(len(BAsuppe))])))
  else:
    fuellzeichenListe = list(set(BAalphabet.replace("ß","ẞ").upper()))

  for zeile in range(len(BAsuppe)):
    for spalte in range(len(BAsuppe[0])):
      if BAsuppe[zeile][spalte] == ".":
        BAsuppe[zeile][spalte] = random.choice(fuellzeichenListe)
        BAleereZellen += 1

  return BAsuppe, BAleereZellen


def buchstabensuppe_zeigen(BZsuppe):
  """
  Gib die Buchstabensuppe im Terminal aus.
  """
  for zeile in range(len(BZsuppe)):
    for spalte in range(len(BZsuppe[0])):
      print(BZsuppe[zeile][spalte], end=" ")
    print()


def svg_output(SOsuppe, SOwortliste=0, SOversuch=0, SOausgelasseneWorte=0,
      SOanzahlUeberlappungen=0, SOanzahlDiagonale=0, SOleereZellen=0, SOloesungswort=""):
  """
  Erzeuge SVG-Datei mit der Buchstabensuppe.
  """

  # maximale Ausdehnung der Suppe feststellen
  lenSuppe = max(len(SOsuppe), len(SOsuppe[0]))

  SVG_HEAD = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="210mm"
   height="297mm"
   viewBox="0 0 744.09448819 1052.3622047"
   id="svg2"
   version="1.1"
   inkscape:version="0.91 r13725"
   sodipodi:docname="buchstabensuppe_vorlage.svg">
  <defs
     id="defs4" />
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="0.39245043"
     inkscape:cx="674.01525"
     inkscape:cy="526.1811"
     inkscape:document-units="px"
     inkscape:current-layer="layer1"
     showgrid="false"
     inkscape:snap-bbox="true"
     inkscape:snap-bbox-midpoints="false"
     inkscape:snap-object-midpoints="false"
     inkscape:snap-page="false"
     inkscape:window-width="1024"
     inkscape:window-height="587"
     inkscape:window-x="0"
     inkscape:window-y="13"
     inkscape:window-maximized="0"
     inkscape:bbox-paths="false"
     inkscape:bbox-nodes="true"
     inkscape:snap-to-guides="false"
     inkscape:object-nodes="true"
     inkscape:snap-intersection-paths="true"
     inkscape:object-paths="true"
     inkscape:snap-smooth-nodes="true"
     inkscape:snap-bbox-edge-midpoints="true" />
  <metadata
     id="metadata7">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Ebene 1"
     inkscape:groupmode="layer"
     id="layer1">
    <text
       xml:space="preserve"
"""
  
  if lenSuppe > 10:
    SVG_HEAD2 = """       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:25.44705391px;line-height:125%;font-family:'Linux Libertine Mono O';-inkscape-font-specification:'Linux Libertine Mono O, Normal';text-align:center;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       x="373.69809"
       y="84.79248"
       id="text3336"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan3399"
         x="373.69809"
         y="84.79248">"""
  else:
    SVG_HEAD2 = """       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:52.73477554px;line-height:125%;font-family:'Linux Libertine Mono O';-inkscape-font-specification:'Linux Libertine Mono O, Normal';text-align:center;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:middle;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       x="373.1199"
       y="102.88439"
       id="text3336"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan3353"
         x="373.11993"
         y="102.88439">"""


  # das was auf eine Suppenzeile folgt (also post linea)
  if lenSuppe > 10:
    SVG_PostLines = [ """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3401" 
         x="373.69809" 
         y="150.71123">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3403" 
         x="373.69809" 
         y="216.62999">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3405" 
         x="373.69809" 
         y="282.54874">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3407" 
         x="373.69809" 
         y="348.4675">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3409" 
         x="373.69809" 
         y="414.38623">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3411" 
         x="373.69809" 
         y="480.30499">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3413" 
         x="373.69809" 
         y="546.22375">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3415" 
         x="373.69809" 
         y="612.14246">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3417" 
         x="373.69809" 
         y="678.06122">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3419" 
         x="373.69809" 
         y="743.97998">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3421" 
         x="373.69809" 
         y="809.89874">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3423" 
         x="373.69809" 
         y="875.8175">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3425" 
         x="373.69809" 
         y="941.73627">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3427" 
         x="373.69809" 
         y="1007.655">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3429" 
         x="373.69809" 
         y="1073.5737">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3431" 
         x="373.69809" 
         y="1139.4924">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3433" 
         x="373.69809" 
         y="1205.4113">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3435" 
         x="373.69809" 
         y="1271.33">""",
      """</tspan><tspan 
         sodipodi:role="line" 
         id="tspan3437" 
         x="373.69809" 
         y="1337.2488">""",
      """</tspan></text>""" ]
  else:
    SVG_PostLines = [ """</tspan><tspan
         sodipodi:role="line"
         id="tspan3355"
         x="373.11993"
         y="171.47337">""",
      """</tspan><tspan
         sodipodi:role="line"
         id="tspan3357"
         x="373.11993"
         y="240.06235">""",
      """</tspan><tspan
         sodipodi:role="line"
         id="tspan3359"
         x="373.11993"
         y="308.65134">""",
      """</tspan><tspan
         sodipodi:role="line"
         id="tspan3361"
         x="373.11993"
         y="377.2403">""",
      """</tspan><tspan
         sodipodi:role="line"
         id="tspan3363"
         x="373.11993"
         y="445.82928">""",
      """</tspan><tspan
         sodipodi:role="line"
         id="tspan3365"
         x="373.11993"
         y="514.41827">""",
      """</tspan><tspan
         sodipodi:role="line"
         id="tspan3367"
         x="373.11993"
         y="583.0072">""",
      """</tspan><tspan
         sodipodi:role="line"
         id="tspan3369"
         x="373.11993"
         y="651.59619">""",
      """</tspan><tspan
         sodipodi:role="line"
         id="tspan3371"
         x="373.11993"
         y="720.18518">""",
      """</tspan></text>""" ]

  SVG_BODY = """    <flowRoot
       xml:space="preserve"
       id="flowRoot3396"
       style="fill:black;stroke:none;stroke-opacity:1;stroke-width:1px;stroke-linejoin:miter;stroke-linecap:butt;fill-opacity:1;font-family:sans-serif;font-style:normal;font-weight:normal;font-size:40px;line-height:125%;letter-spacing:0px;word-spacing:0px"><flowRegion
         id="flowRegion3398"><rect
           id="rect3400"
           width="629.37885"
           height="295.57874"
           x="61.154221"
           y="700.72546" /></flowRegion><flowPara
         id="flowPara3402" /></flowRoot>    <flowRoot
       xml:space="preserve"
       id="flowRoot3412"
       style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:"""

  SVG_BODY2 = """px;line-height:125%;font-family:'Linux Libertine O';-inkscape-font-specification:'Linux Libertine O';letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       transform="translate(3.1040283,123.53632)"><flowRegion
         id="flowRegion3414"><rect
           id="rect3416"
           width="614.09033"
           height="280.29025"
           x="63.702312"
           y="611.54218"
           style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-family:'Linux Libertine O';-inkscape-font-specification:'Linux Libertine O'" /></flowRegion><flowPara
         id="flowPara3418">"""

  # hier steht die Zahl der versteckten Wörter
  # Standard-Text könnte sein: »Finde xx Wörter:«
  SVG_PostNumberOfWords = """</flowPara><flowPara
         id="flowPara3420">"""

  # hier steht die Liste der vesteckten Wörter
  SVG_TAIL = """</flowPara></flowRoot>  </g>
</svg>"""

  ###############################
  # bis hier SVG-Text definiert #
  ###############################

  if type(SOwortliste) is int:
    anzahlWorte = SOwortliste
  else:
    SOwortliste = list(set(SOwortliste)) # um Dopplungen zu verhindern
    anzahlWorte = len(SOwortliste)
  
  ausgabeDateiname = ( "Buchstabensuppe___"+
    str(len(SOsuppe[0]))+"x"+str(len(SOsuppe))+
    "_Worte"+str(anzahlWorte)+
    "_Versuche"+str(SOversuch)+
    "_AusgelasseneWorte"+str(SOausgelasseneWorte)+
    "_Überlappungen"+str(SOanzahlUeberlappungen)+
    "_Diagonale"+str(SOanzahlDiagonale)+
    "_LeereZellen"+str(SOleereZellen) )

  if len(SOloesungswort) > 0:
      ausgabeDateiname += "_Lösungswort"+str(SOloesungswort)

  ausgabeDateiname += ".svg"

  with open(ausgabeDateiname, 'w') as svgfile:
    svgfile.write(SVG_HEAD)
    svgfile.write(SVG_HEAD2)

    for teiltextNr in range(len(SVG_PostLines)):
      if teiltextNr < len(SOsuppe):
        for einzelBuchstabe in SOsuppe[teiltextNr]:
          svgfile.write(einzelBuchstabe+" ")
      else:
        svgfile.write(" ")
      svgfile.write(SVG_PostLines[teiltextNr])

    svgfile.write(SVG_BODY)

    # ermitteln der Anzahl der Zeichen in der Aufzählung der Wörter
    if not type(SOwortliste) is int:
      # nach letztem Wort kommt kein Komma und Leerzeichen
      lenListOfWords = -2
      for einWort in SOwortliste[:-1]:
        # es soll immer noch ein Komma und Leerzeichen (= zwei Zeichen) hinter
        # jedes Wort
        lenListOfWords += len(einWort) + 2
    else:
      lenListOfWords = 0

    # Wenn die durch Komma getrennte Aufzählung der Wörter zu lang ist, dann
    # Schriftgröße der Aufgabenstellung verringern
    if lenListOfWords > 130:
      svgfile.write("28")
    else:
      svgfile.write("40")

    svgfile.write(SVG_BODY2)

    if type(SOwortliste) is int:
      if SOwortliste == 0:
        svgfile.write("Suche so viele Wörter wie möglich!")
        svgfile.write(SVG_PostNumberOfWords)
        svgfile.write(" ")
      else:
        svgfile.write("Finde "+str(SOwortliste)+" Wörter.")
        svgfile.write(SVG_PostNumberOfWords)
        svgfile.write("Nur die Anzahl der Wörter wird verraten, aber nicht welche!")

    else:
      svgfile.write("Finde "+str(len(SOwortliste))+" Wörter:")
      svgfile.write(SVG_PostNumberOfWords)

      # Liste der Wörter mit Komma getrennt
      for einWort in SOwortliste[:-1]:
        svgfile.write(einWort+", ")
      svgfile.write(SOwortliste[-1])

    svgfile.write(SVG_TAIL)


def test():
  """
  Hier wurden ein paar Wortlisten getestet, die für die Entwicklung
  verwendet wurden.
  """
  # Größe der Suppe
  anzahl_spalten = 16  # x-koordinate
  anzahl_zeilen = 12    # y-koordinate
  min_diagonale = 0

  #wortliste = wortereinlesen(min(anzahl_spalten, anzahl_zeilen))
  #wortliste = ["erik", "lilli", "pine", "kamo", "kosta"] # 5,4 5,5,2
  #wortliste = ["julia", "erik", "lilli", "pine", "kamo", "kosta", "mareike", "strubbi", "oma", "julia", "lia"] # 7,6,0 7,7
  #wortliste = ["erik", "lilli", "pine", "kamo", "juan", "lia"] # 5,4,1
  #wortliste = ["erik", "lilli", "pine", "kamo", "juan", "mareike", "strubbi", "hahn", "laila", "maxim", "lia", "oma", "opa", "giuno", "kevin", "alix"] # 8,8
  #wortliste = ["erik", "lilli", "pine", "kamo", "juan", "mareike", "strubbi", "hahn", "laila", "maxim", "lia", "oma", "opa", "giuno", "kevin", "alix", "johanna"] # 9,8 9,9 10,8
  #wortliste = ["erik", "lilli", "pine", "kamo", "juan", "mareike", "strubbi", "hahn", "laila", "maxim", "lia", "oma", "opa", "giuno", "kevin", "alix", "johanna", "julia", "jojo", "ine", "marion", "eutimio"] # 10,9 10,10
  #wortliste = ["Berlin", "Mainz", "Villingen", "Hamburg", "München", "Frontera", "Valverde", "Zürich"] # 9,8
  wortliste = ["Kartoffelbrei","Quiche","Bonbon","Toast","Fischstäbchen","Kakao","Pommes","Bratkartoffel","Waffel","Pfannkuchen","Gummibärchen","Mangoeis","Limonade","Nachtisch","Maracuja","Erdbeermarmelade","Streusel","Keks","Schokocreme","Melone","Ketchup","Mandel"] # 16,12


  print(wortliste, len(wortliste))
  for i in range(1):
    suppe, versuch, anzahlWorte, ausgelasseneWorte, anzahlUeberlappungen, anzahlDiagonale = (
      buchstabensuppe_erzeugen(wortliste, anzahl_spalten, anzahl_zeilen,
        BEerlaubteVersuche=100000, BEminDiagonale=min_diagonale) )
    print()
    print("Versuche:", versuch)
    if ausgelasseneWorte > 0:
      print("Ausgelassene Worte:", ausgelasseneWorte)
    if anzahlUeberlappungen > 0:
      print("Überlappungen:", anzahlUeberlappungen)
    if anzahlDiagonale > 0:
      print("Diagonale:", anzahlDiagonale)
    print("Ausmaße:", anzahl_spalten, "mal", anzahl_zeilen)

    # nur die verteilten Wörter zeigen
    buchstabensuppe_zeigen(suppe)

    print(80*"=")

    suppe, leereZellen = buchstabensuppe_auffuellen(suppe)
    print("Leere Zellen:", leereZellen)

    # aufgefüllte Matrix zeigen
    buchstabensuppe_zeigen(suppe)

    print(80*"=")

  svg_output(suppe, wortliste, versuch, ausgelasseneWorte,
      anzahlUeberlappungen, anzahlDiagonale, leereZellen)


def controller():
  global VERBOSE
  p = argparse.ArgumentParser(description='Eine Buchstabensuppe erzeugen')
  p.add_argument('--version',
                  action='version',
                  version='0.20160428')
  p.add_argument('wortliste',
                  action='store',
                  nargs='+',
                  metavar="WORT",
                  help='Ein Wort, dass in einer Suppe von Buchstaben verteilt werden voll. Es können mehrere Wörter durch Leerzeichen getrennt übergeben werden, zum Beispiel: Hund Katze Maus')
  p.add_argument('--dimensionen','-d',
                  action='store',
                  nargs=2,
                  type=int,
                  default=(20,20),
                  metavar=("SPALTEN","ZEILEN"),
                  help='Größe der Buchstabensuppe, also Anzahl Zeilen und Anzahl Spalten, zum Beispiel: 10 8, Standard: 20 20')
  p.add_argument('--diagonale','-g',
                  action='store',
                  type=int,
                  default=0,
                  help='Anzahl der mindestens vorkommenden diagonal geschriebenen Wörter, Standard: 0')
  p.add_argument('--alphabet','-a',
                  action='store',
                  type=str,
                  default=string.ascii_uppercase,
                  help='Zu verwendende Buchstaben, um leere Zellen aufzufüllen, Standard: Alle Buchstaben des Alphabets')
  p.add_argument('--loesungswort','-l',
                  action='store',
                  type=str,
                  default='',
                  help='Lösungswort, dessen Buchstaben in die leeren Zellen verteilt werden')
  p.add_argument('--versuche','-r',
                  action='store',
                  type=int,
                  default=1000,
                  help='Anzahl der Versuche, alle Wörter zufällig zu verteilen, Standard: 1000')
  p.add_argument('--verbose', '-v',
                  action='store_true',
                  default=False,
                  help='Das Programm verhält sich gesprächig und zeigt Statusmeldungen und Zwischenergebnisse')
  p.add_argument('--svg', '-s',
                  action='store_true',
                  default=False,
                  help='Das Programm erzeugt eine SVG-Datei')

  arguments = p.parse_args()
  
  VERBOSE = arguments.verbose

  anzahl_spalten = arguments.dimensionen[0]
  anzahl_zeilen = arguments.dimensionen[1]

  # Suppendimension zu klein?
  lenWortliste = max([len(i) for i in arguments.wortliste])
  if lenWortliste > anzahl_spalten and lenWortliste > anzahl_zeilen:
    print("FEHLER! Die Wörter dürfen höchstens "+
        str(max(anzahl_spalten, anzahl_zeilen))+" Zeichen haben.")
    sys.exit(2)

  if VERBOSE:
    print(arguments)

  suppe, versuch, anzahlWorte, ausgelasseneWorte, anzahlUeberlappungen, anzahlDiagonale = (
    buchstabensuppe_erzeugen(arguments.wortliste, anzahl_spalten, anzahl_zeilen,
      BEerlaubteVersuche=arguments.versuche, BEminDiagonale=arguments.diagonale) )

  if VERBOSE:
    print()
    print("Versuche:", versuch)
    print("Wörter:", anzahlWorte)
    if ausgelasseneWorte > 0:
      print("Ausgelassene Worte:", ausgelasseneWorte)
    if anzahlUeberlappungen > 0:
      print("Überlappungen:", anzahlUeberlappungen)
    if anzahlDiagonale > 0:
      print("Diagonale:", anzahlDiagonale)
    print("Ausmaße:", anzahl_spalten, "mal", anzahl_zeilen)

    # nur die verteilten Wörter zeigen
    buchstabensuppe_zeigen(suppe)

    print(80*"=")

  if len(arguments.loesungswort) > 0:
    suppe = buchstabensuppe_loesungswort(suppe, arguments.loesungswort)

    if VERBOSE:
      print("Lösungswort:", arguments.loesungswort)
      # mit dem Lösungswort sieht es so aus
      buchstabensuppe_zeigen(suppe)

      print(80*"=")

  suppe, leereZellen = buchstabensuppe_auffuellen(suppe, BAalphabet=arguments.alphabet)

  if VERBOSE:
    print("Leere Zellen:", leereZellen)

  # aufgefüllte Matrix zeigen
  buchstabensuppe_zeigen(suppe)

  if arguments.svg:
    svg_output(suppe, arguments.wortliste, versuch, ausgelasseneWorte,
      anzahlUeberlappungen, anzahlDiagonale, leereZellen, arguments.loesungswort)


def main():
  controller()


########
# MAIN #
########
if __name__ == "__main__":
  main()
