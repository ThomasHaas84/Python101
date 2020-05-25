
# Neun_Leben
# Konsolenspiel


import random


leben = 9
wörter = ["Zwölf", "Pilze", "Braut", "Tante", "Sorge", "Otter", "Pferd", "Zwang", "Quarz", "Speck", "Ecken", "Autos",
          "Säule", "Angel", "jetzt", "Kampf", "Münze", "Walze", "joggen", "bauen", "leben", "kauen", "Pizza", "Busch"]
geheim_wort = random.choice(wörter)
verdeckt_wort = list('?????')
herz = u'\u2764'
wort_richtig_geraten = False


def aktu_verdeckt(buchstabe_geraten, geheim_wort, verdeckt_wort):
    index = 0
    while index < len(geheim_wort):
        if buchstabe_geraten == geheim_wort[index]:
            verdeckt_wort[index] = buchstabe_geraten
        index += 1

while leben > 0:
    print(verdeckt_wort)
    print("Verbleibende Leben: " + herz * leben)
    raten = input("Rate einen Buchstaben oder das Wort: ")

    if raten == geheim_wort:
        wort_richtig_geraten = True
        break

    elif raten in geheim_wort:
        aktu_verdeckt(raten, geheim_wort, verdeckt_wort)
    else:
        print("Falsch. Ein Leben weniger.")
        leben -= 1

if wort_richtig_geraten:
    print("Gewonnen! Das geheime Wort war " + geheim_wort)
else:
    print("Leider verloren! Das geheime Wort war " + geheim_wort)

