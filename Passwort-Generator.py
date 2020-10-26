
# Passwort-Generator
# Konsolenprogramm zum erstellen zufälliger Passwörter


import random


die_adjektive = ["müd", "wach", "schnell", "langsam", "feucht", "trocken", "stinkend", "müffelnd", "heiß", "kalt",
                 "fett", "dick", "dünn", "klein", "winzig", "groß", "riesig", "schaumig", "schwurbelig", "krümmelig",
                 "schleimig", "klebrig", "flauschig", "schläfrig", "glatt", "eckig", "rund", "weiß", "schwarz",
                 "rot", "grün", "blau", "gelb", "lilafarben", "rosafarben", "durchsichtig", "heiß", "kalt", "krank",
                 "abstinent", "alkoholisch", "akkurat", "automatisch", "bairisch", "bankrott", "behaglich", "bunt",
                 "brilliant", "blind", "charmant", "chemisch", "christlich", "chronisch", "cremefarben", "dankbar",
                 "deckend", "darstellbar", "demokratisch", "depressiv", "derb", "diebisch", "edl", "effizient",
                 "egoistisch", "ehrfürchtig", "ehrgeizig", "ehrlos", "einladend", "evangelisch", "elektrisch",
                 "fachkundig", "fantasielos", "fein", "fettig", "fad", "fitt", "flott", "flach", "geisterhaft",
                 "gleichberechtigt", "glücklich", "haarig", "hündisch", "hyperaktiv", "idyllisch", "imaginär",
                 "individuell", "integriert", "jodhaltig", "jüdisch", "jugendlich", "jungfräulich", "juristisch",
                 "kahl", "käuflich", "keusch", "knackig", "kokett", "kontrovers", "künstlich", "labbrig", "lieb",
                 "luxuriös", "mächtig", "meisterlich", "mystisch", "nächtlich", "negativ", "niveaulos", "notdürftig",
                 "obsolet", "ökologisch", "öffentlich", "österlich", "pädagogisch", "peinlich", "pensioniert",
                 "poetisch", "provokant", "quirlig", "radikal", "recyclebar", "rhythmisch", "roh", "salzig",
                 "spitz", "sympathisch", "temperamentvoll", "traditionell", "typisch", "trotzig", "utopisch",
                 "umständlich", "verantwortungslos", "verklemmt", "vulgär", "wahlberechtigt", "weich", "weihnachtlich",
                 "wohnlich", "x-beliebig", "youtubebegeistert", "zappelig", "zart", "behaart", "zickig", "zuckerfrei",
                 "zynisch", "lang", "verdorben", "schimmelig", "eutroph", "radioaktiv", "fies", "versifft",
                 "nazifiziert", "gekreuzigt", "hessisch", "schwäbisch", "sächsisch", "artig", "frivol", "anstößig",
                 "alt", "rostig", "aphrodisierend", "abenteuerlustig", "athletisch", "attraktiv", "schamlos",
                 "bedeutend", "beglückend", "bezaubernd", "charaktervoll", "dominant", "einfühlsam", "elegant",
                 "emotional", "erfrischend", "erotisch", "familiär", "fesselnd", "freizügig", "fürsorglich",
                 "gastfreundlich", "geduldig", "geschmackvoll", "gigantisch", "grenzenlos", "atemlos", "hochbegabt",
                 "hübsch", "hässlich", "intensiv", "international", "kostbar", "lässig", "lebensbejahend",
                 "märchenhaft", "motivierend", "ökonomisch", "phantastisch", "persönlich", "pikant", "potent",
                 "fruchtbar", "prächtig", "prall", "hochsensibl", "quicklebendig", "rassig", "rasant", "raffiniert",
                 "real", "surreal", "sagenumwoben", "sanft", "spannend", "stilvoll", "stürmisch", "sündig", "taktisch",
                 "teamfähig", "überdurchschnittlich", "überzeugend", "unsterblich", "unwiderstehlich",
                 "verantwortungsvoll", "verbindlich", "verführerisch", "wortgewandt", "warmherzig", "wertvoll",
                 "zauberhaft", "zaghaft", "zeitlos", "zuverlässig", "zwischenmenschlich", "grotesk", "faschistoid",
                 "kafkaesk", "aromatisch", "giftig", "faltig", "diskret", "zerknirscht", "gedehnt", "gespreitzt",
                 "schüchtern", "locker", "tollpatschig", "anmaßend", "auferstanden", "verzaubert", "verlaust",
                 "hollisch", "promoviert", "erzkonservativ", "rechtspopulistisch", "elitär", "devot", "sexistisch",
                 "homophob", "rechtsradikal", "linksradikal", "linksversifft", "islamistisch", "rassistisch",
                 "knauserig", "geizig", "akribisch", "beharrlich", "beispiellos", "belastbar", "arbeitsscheu",
                 "berauschend", "stets_bemüht", "bescheiden", "besonnen", "bewunderungswürdig", "bildhübsch",
                 "bodenständig", "charakterstark", "charismatisch", "deliziös", "englisch", "französisch", "spanisch",
                 "italienisch", "indisch", "ostdeutsch", "westdeutsch", "niederländisch", "holländisch", "höllisch",
                 "außerirdisch", "marsianisch", "skandinavisch", "schwäbisch", "divenhaft", "dogmatisch",
                 "dominant", "durchtrieben", "effektiv", "ehrwürdig", "eigenwillig", "eindrucksvoll", "einwandfrei",
                 "eloquent", "emotional", "empathisch", "engelsgleich", "entgegenkommend", "entscheidungsfreudig",
                 "erfolgsorientiert", "erlebnisreich", "erträglich", "experimentierfreudig", "exzentrisch",
                 "facettenreich", "fehlerfrei", "festlich", "freiheitsliebend", "freizügig", "fundamental",
                 "gebildet", "galant", "gediegen", "gefühlsbetont", "geradlinig", "geschmeidig", "glaubensstark",
                 "gönnerhaft", "grazil", "harmonisch", "hochanständig", "hochmodern", "idealistisch", "konkurrenzlos",
                 "krisenfest", "leistungsorientiert", "liebreizend", "lösungsorientiert", "modebewusst",
                 "obligatorisch", "paradiesisch", "phänomenal", "prinzipientreu", "prophetisch", "raumfüllend",
                 "rekordverdächtig", "respektiert", "schlagfertig", "skandalös", "sinnlich", "sozialverträglich",
                 "spielerisch", "spritzig", "stimmungsvoll", "strategisch", "stürmisch", "sündig", "sympathisch",
                 "tiefgründig", "traditionell", "überdurchschnittlich", "übersinnlich", "unbestechlich",
                 "unkompliziert", "unkonventionell", "unproblematisch", "unverfälscht", "verblüffend", "verführerisch",
                 "verspielt", "verträumt", "vielschichtig", "vorbildlich", "vortrefflich", "vorurteilsfrei",
                 "vorzeigenswert", "wohlschmeckend", "wohlverdient", "würdevoll", "zauberhaft", "zeitlos",
                 "zukunftsorientiert", "unzurechnungsfähig", "deftig", "gesalzen", "süß", "scharf", "gedemütigt",
                 "zerissen", "gebrochen", "verwirrt", "sehr_verwirrt", "extrem_verwirrt", "inkontinent", "unfähig",
                 "dement", "laktosefrei", "fettfrei", "fettreduziert", "dreieckig", "viereckig", "verzweifelt",
                 "unerfahren", "kindisch", "bipolar", "sadistisch", "erregend", "blasphemisch", "zärtlich",
                 "destruktiv", "verwöhnt",
                 ]





die_nomen = ["der_Bagger", "der_Elefant", "das_Einhorn", "die_Kuh", "die_Maus", "die_Feder", "der_Vogel", "das_Haus",
             "die_Fledermaus", "das_Handy", "die_Ratte", "die_Seekuh", "der_Floh", "das_Flugzeug", "das_Schiff",
             "das_Buch", "die_Lampe", "das_Kabel", "der_Lötkolben", "die_Zange", "der_Schraubenzieher",
             "der_Kopfhörer", "der_Mundschutz", "der_Virus", "der_Käfer", "die_Schlange", "der_Bär", "das_Nashorn",
             "das_Erdmännchen", "die_Fernbedienung", "die_Tastatur", "die_Maus", "der_Controller", "der_Monitor",
             "der_Farbdrucker", "der_Esel", "die_Schnecke", "die Biene", "die Laus", "die Elster",
             "das Schwein", "der Bulle", "die Brust", "der Kolben", "der Nippel", "die Stange", "die Toilette",
             "die Zahnbürste", "das Handtuch", "der Mülleimer", "das Senfglas", "die Gurke", "die Tomate",
             "der Hase", "das Huhn", "der Hahn", "die Hose", "die Socke", "die Frisur", "das Schnitzel", "die Wurst",
             "der Käse", "die Butter", "der Fingernagel", "die Nase", "die Spalte", "das Loch", "der Bauchnabel",
             "das Ei", "der Sack", "der Bart", "das Taschentuch", "der Mann", "die Frau", "das Ding", "die Sache",
             "der Nagel", "das Fahrrad", "die Biene", "die Scheibe", "die Knolle", "der Ofen", "die Heizung",
             "der Rauchmelder", "der Stuhl", "das Sofa", "die Matratze", "der Toaster", "die Gabel", "der Löffel",
             "das Säugetier", "der Fisch", "die Spinne", "der Elf", "der Mensch", "das Kind", "das Baby", "der Ork",
             "die Hexe", "der Zauberer", "die Tür", "das Fenster", "der Eistee", "der Kaffee", "die Milch", "das Bier",
             "das Brot", "das Duschgel", "das Klebeband", "der Handschuh", "die Socke", "das Telefon", "der Müll",
             "der Dreck", "die Kotze", "das Proton", "das Neutron", "das Elektron", "die Galaxie", "der Stern",
             "der Himmel", "die Wolke", "die Sonne", "die Rakete", "das Raumschiff", "die Bakterie", "das Molekül",
             "der Wurm", "die Nacktschnecke", "die Eismaschine", "der Gartenzaun", "der Nacktmulch", "das Schnabeltier",
             "die Eiscremewaffel", "der Autositz", "der Fahrradhelm", "das Nudelsieb", "das Nudelholz",
             "die Nähmaschine", "der Liegestuhl", "der Vulkan", "die Zimmerpflanze", "das Badesalz", "das Eisenatom",
             "das Goldplättchen", "der Wattebausch", "die Handtasche", "der Baum", "die Stulle", "die Stute",
             "das Staubkorn", "der Waschlappen", "das Herzchen", "die Bierflasche", "der Weinkorken", "das Klopapier",
             "die Windel", "das Feuchttuch", "der Bollerwagen", "der Busch", "die Blume", "das Opfer", "das Ladekabel",
             "das Lätzchen", "der Roboter", "der Kühlschrank", "die Leberwurst", "der Erdbeerkäse", "der Saugroboter",
             "die Hausaufgabe", "die Kurzgeschichte", "das Schwert", "das Trauerspiel", "die Hüpfburg", "die Unordnung",
             "das Saufgelage", "die Mistgabel", "das Scheunentor", "die Matheklausur", "das Veilchen", "das Brettspiel",
             "der Gartenstrand", "der Anfall", "die Schublade", "die Zumutung", "die Anmaßung", "die Erniedrigung",
             "die Straftat", "das Vermächtnis", "das Urlaubsziel", "das Lastenfahrrad", "der Arzt", "der Pinselstrich",
             "der Tretroller", "die Spuckekugel", "der Ökofritze", "der Junge", "die Tussi", "die Prostituierte",
             "die Schlampe", "der Rollladen", "das Elfenohr", "die Peperoni", "die Babykotze", "die Dekoration",
             "der Waschbär", "der Seelöwe", "der Pinguin", "die Brustwarze", "die Nippelcreme", "die Vergewaltigung",
             "der Maschendrahtzaun", "die Oberflächenspannung", "die Anomalie", "das Periodensystem", "die Periode",
             "die Ionisierungsenergie", "der Trinkwasserspender", "der Brüllaffe", "der Auswurf",
             "der Geschenkgutschein", "die Vernichtung", "die Auslöschung", "die Strahlung", "die Agression",
             "die Akupunktur", "der Alptraum", "das Ärgernis", "die Symmetrie", "die Ballerina", "die Geiselnahme",
             "die Steinigung", "die Wiederauferstehung", "der Kanibale", "die Katastrophe", "die Rose", "das Rentier",
             "das Rückgrat", "das Speisesalz", "die Säure", "die Familie", "die Zucchini", "das Anhängsel",
             "das Edelgas", "der Tumor", "der Ausschlag", "der Ökogrill", "der_Hippie", "die Rosette", "die Eichel",
             "die Quecksilbersäule", "der Homöopath", "die Sau", "der Geizhals", "die Hausfrau", "der Hausmann",
             "das Zimmermädchen", "der Schwanz", "die Röhre", "die Gießkanne", "das Staubkorn", "die Blase",
             "die Schraube", "die Kotstulle", "der Rieseneinlauf", "das Eichhörnchen", "der Seestern",
             "die Blumenwiese", "der Brechreiz", "der Würgereflex", "der Symmetriebruch", "der Schweißausbruch",
             "der Eiswürfel", "der Kaffeebecher", "der Saftsack", "der Schnellkochtopf", "der Weihnachtskot",
             "die Warze", "die Weltanschauung", "die Chilischote", "die Kontrollgruppe", "die Vertrauensperson",
             "der Partner", "der Atompilz", "das Abenteuer", "das Geständnis", "die Beichte", "die Nachtwache",
             "die Pflaume", "die Hölle", "der Schrank", "die Lampe", "die Flasche", "die Tasche", "der Schuh",
             "der Ball", "der Ballettschuh", "die Krone", "die Münze", "der Ausfluss", "der Geldschein", "der Pickel",
             "die Kloschüssel", "die Klobürste", "das Toilettenpapier", "das Einhorn", "die Einhornscheiße",
             "die Bremsstrahlung", "der Hautausschlag", "das Sexspielzeug", "das Wurstwasser", "der Laborunfall",
             "der Krabbenburger", "der Schwamm", "die Krabbe", "der Gebrauchtwagenhändler", "der Massagestab",
             "der Autounfall", "der Stift", "die Rutsche", "der Zehennagel", "die Fernbedienung",
             ]


symbole = ["#", "&", "%", "§", "?", "!", "/", "$", "€", "*", ]


# Doppelgänger in Listen entfernen
die_nomen = list(set(die_nomen))
die_adjektive = list(set(die_adjektive))


# Programmvorstellung (wird einmalig bei Programmstart angezeigt)
print()
print("-" * 33)
print("Willkommen im Passwort-Generator!")
print("-" * 33)
print(len(die_adjektive), "Adjektive")
print(len(die_nomen),  "Nomen")
print("10.000 Zahlen")
print(len(symbole), "Symbole")
print()
print(str(f'{len(die_adjektive) * len(die_nomen) * len(symbole) * 10000:,}') + " Kombinationsmöglichkeiten!")


# Hauptschleife
while True:
    adjektiv = random.choice(die_adjektive)
    nomen = random.choice(die_nomen)
    symbol = random.choice(symbole)
    gender = ""
    if nomen[1] == "i":
        gender = "e"
    elif nomen[1] == "e":
        gender = "er"
    else:
        gender = "es"
    zahl = random.randrange(1000, 10000)
    nomen = nomen[4:]
    passwort = adjektiv + gender + "_" + nomen + "_" + str(zahl) + symbol
    print()
    print("________________________")
    print("Das neue Passwort lauet: ")
    print()
    print(passwort)
    print()
    antwort = input()
    if antwort == "q":
        break


