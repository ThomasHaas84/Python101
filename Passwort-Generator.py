
# Passwort-Generator
# Konsolenprogramm zum erstellen zufälliger Passwörter


import random
import string


die_adjektive = ["müde", "wach", "schnell", "langsam", "feucht", "trocken", "stinkend", "müffelnd", "heiß", "kalt",
             "fett", "dick", "dünn", "klein", "winzig", "groß", "riesig", "schaumig", "schwurbelig", "krümmelig",
             "schleimig", "klebrig", "flauschig", "schläfrig", "glatt", "eckig", "rund", "weiß", "schwarz",
             "rot", "grün", "blau", "geld", "lila", "rosa", "durchsichtig", "heiß", "kalt", "krank", "abstinent",
             "alkoholisch", "akkurat", "automatisch", "bairisch", "bankrott", "behaglich", "bunt", "brillant",
             "blind", "charmant", "chemisch", "christlich", "chronisch", "cremefarben", "dankbar", "deckend",
             "darstellbar", "demokratisch", "depressiv", "derb", "diebisch", "edel", "effizient", "egoistisch",
             "ehrfürchtig", "ehrgeizig", "ehrlos", "einladend", "evangelisch", "elektrisch", "fachkundig", "fantasielos",
             "fein", "fettig", "fad", "fit", "flott", "flach", "geisterhaft", "gleichberechtigt", "glücklich", "haarig",
             "hündisch", "hyperaktiv", "idyllisch", "imaginär", "individuell", "integriert", "jodhaltig", "jüdisch",
             "jugendlich", "jungfräulich", "juristisch", "kahl", "käuflich", "keusch", "knackig", "kokett", "kontrovers",
             "künstlich", "labberig", "lieb", "luxuriös", "mächtig", "meisterlich", "mystisch", "nächtlich", "negativ",
             "niveaulos", "notdürftig", "obsolet", "ökologisch", "öffentlich", "österlich", "pädagogisch", "peinlich",
             "pensioniert", "poetisch", "provokant", "quirlig", "radikal", "recyclebar", "rhythmisch", "roh", "salzig",
             "spitz", "sympathisch", "temperamentvoll", "traditionell", "typisch", "trotzig", "utopisch", "umständlich",
             "verantwortungslos", "verklemmt", "vulgär", "wahlberechtigt", "weich", "weihnachtlich", "wohnlich",
             "x-beliebig", "youtubebegeistert", "zappelig", "zart", "behaart", "zickig", "zuckerfrei", "zynisch", "lang",
             "verdorben", "schimmelig", ]


die_nomen = ["Bagger", "Elefant", "Einhorn", "Kuh", "Maus", "Feder", "Vogel", "Haus", "Fledermaus", "Handy", "Ratte",
         "Seekuh", "Floh", "Flugzeug", "Schiff", "Buch", "Lampe", "Kabel", "Lötkolben", "Zange", "Schraubenzieher",
         "Kopfhörer", "Mundschutz", "Virus", "Käfer", "Schlange", "Bär", "Nashorn", "Erdmännchen", "Fernbedienung",
         "Tastatur", "Maus", "Controller", "Monitor", "Drucker", "Esel", "Schnecke", "Biene", "Laus", "Elster",
         "Schwein", "Bulle", "Brust", "Kolben", "Nippel", "Stange", "Toilette", "Zahnbürste", "Handtuch", "Mülleimer",
         "Senfglas", "Gurke", "Tomate", "Hase", "Huhn", "Hahn", "Hose", "Socke", "Frisur", "Schnitzel", "Wurst",
         "Käse", "Butter", "Fingernagel", "Nase", "Spalte", "Loch", "Bauchnabel", "Ei", "Sack", "Bart", "Taschentuch",
         "Mann", "Frau", "Ding", "Sache", "Nagel", "Fahrrad", "Biene", "Scheibe", "Knolle", "Ofen", "Heizung", "Rauchmelder",
         "Stuhl", "Sofa", "Matratze", "Toaster", "Gabel", "Löffel", "Säugetier", "Fisch", "Spinne", "Elf", "Mensch", "Kind",
         "Baby", "Ork", "Hexe", "Zauberer", "Tür", "Fenster", "Eistee", "Kaffee", "Milch", "Bier", "Brot", "Duschgel",
         "Klebeband", "Handschuh", "Socke", "Telefon", "Müll", "Dreck", "Kotze", "Proton", "Neutron", "Elektron",
         "Galaxie", "Stern", "Himmel", "Wolke", "Sonne", "Rakete", "Raumschiff", "Bakterie", "Molekül", "Wurm", "Nacktschnecke",
         "Nacktmulch", "Schnabeltier", "Eiscremewaffel", "Autositz", "Fahrradhelm", "Nudelsieb", "Nudelholz", "Nähmaschine",
         "Badesalz", "Eisenatom", "Goldplättchen", "Wattebausch", "Handtasche", "Baum", "Stulle", "Stute", "Staubkorn",
         "Herzchen", "Bierflasche", "Weinkorken", "Klopapier", "Windel", "Feuttuch", "Bollerwagen", ]


print()
print("Willkommen im Passwort-Generator!")
print()
print(len(die_adjektive), "Adjektive")
print(len(die_nomen),  "Nomen")


while True:
    adjektiv = random.choice(die_adjektive)
    nomen = random.choice(die_nomen)
    zahl = random.randrange(0, 100)
    sonderz = random.choice(string.punctuation)

    passwort = adjektiv + "_" + nomen + "_" + str(zahl) + sonderz
    print()
    print("Das neue Passwort ist:  ", passwort)
    print()
    antwort = input("Beliebige Taste für neues Passwort, 'n' zum Beenden: ")
    if antwort == "n":
        break

