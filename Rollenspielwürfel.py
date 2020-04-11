
# Rollenspielwürfel
# Konsolenwürfel mit beliebiger Würfelgröße


import random

# Hauptschleife
run = True
while run:
    print("-" * 24)
    print("Rollenspielwürfel")
    print("-" * 24)

    # Anfangszahl
    eingabe_A = True
    while eingabe_A:
        A = (input("\nAnfangszahl eingeben: "))
        try:
            A = int(A)
        except:
            ValueError
            print("Falsche Eingabe.")
        else:
            eingabe_A = False

    # Endzahl
    eingabe_E = True
    while eingabe_E:
        E = (input("Endzahl eingeben: "))
        try:
            E = int(E)
        except:
            ValueError
            print("Falsche Eingabe.")
        else:
            eingabe_E = False

    # Zahl würfeln
    Zahl = random.randint(A, E)

    print("-" * 24)
    print("Die gewürfelte Zahl ist: " + str(Zahl))
    print("-" * 24)
    print()


    # Programm beenden
    if input("Beliebige Taste zum Würfeln drücken.\n q zum beenden drücken.") == "q":
        break


















