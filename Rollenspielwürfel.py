
# Rollenspielwürfel
# Konsolenwürfel mit beliebiger Würfelgröße 


import random


def würfel(würfelzahl: int = 1, seiten: int = 6):
    würfel_liste = []
    if würfelzahl == 1:
        print()
        print("Ein", seiten, "seitiger Würfel rollt:")
    else:
        print()
        print(würfelzahl, seiten, "seitige Würfel rollen:")
    try:
        while 0 < würfelzahl < 100:
            x = random.randint(1, seiten)
            würfel_liste.insert(0, x)
            würfelzahl -= 1
        würfel_liste.sort()
        print(würfel_liste)
    except:
        print("Keine Ahnung, wie ich das würfeln soll.")


















