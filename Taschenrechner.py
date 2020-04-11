
# Taschenrechner
# Konsolentaschenrechner mit Error handling


# Hauptschleife
main_loop = True
while main_loop:
    print("-" * 30)
    print("Taschenrechner v1.1")
    print("-" * 30)
    print()

    # Erste Zahl
    schleife_Z1 = True
    while schleife_Z1:
        zahl_1 = (input("Erste Zahl eingeben:  "))
        try:
            zahl_1 = float(zahl_1)
        except ValueError:
            print('Falsche Eingabe.')
        else:
            schleife_Z1 = False

    # Rechenoperation
    schleife_op = True
    while schleife_op:
        operation = (input("\nRechenoperation wählen:\n Addition:           +\n Subtraktion:        -\n Multiplikation:     *\n Division:           /\n "
                           "Faktorisierung:     **\n Division ohne Rest: //\n Modulo:             %\n "))
        if operation == "+":
            schleife_op = False
        elif operation == "-":
            schleife_op = False
        elif operation == "*":
            schleife_op = False
        elif operation == "/":
            schleife_op = False
        elif operation == "**":
            schleife_op = False
        elif operation == "//":
            schleife_op = False
        elif operation == "%":
            schleife_op = False
        else:
            print("Falsche Eingabe.")

    # Zweite Zahl
    schleife_Z2 = True
    while schleife_Z2:
        zahl_2 = (input("Zweite Zahl eingeben:  "))
        try:
            zahl_2 = float(zahl_2)
        except ValueError:
            print("Falsche Eingabe.")
        else:
            schleife_Z2 = False

    print("-" * 30)
    try:
        if operation == "+":
            ergebnis = zahl_1 + zahl_2
        elif operation == "-":
            ergebnis = zahl_1 - zahl_2
        elif operation == "*":
            ergebnis = zahl_1 * zahl_2
        elif operation == "/":
            ergebnis = zahl_1 / zahl_2
        elif operation == "**":
            ergebnis = zahl_1 ** zahl_2
        elif operation == "//":
            ergebnis = zahl_1 // zahl_2
        elif operation == "%":
            ergebnis = zahl_1 % zahl_2
    except ZeroDivisionError:
        print("Kann leider nicht berechnet werden.")
        zahl_2 = 0
        ergebnis = "undefiniert"

    try:
        print(zahl_1, operation, zahl_2, " = ", ergebnis)
        print("-" * 30)
    except ValueError:
        pass


    # Beenden des Programms
    if input("Beliebige Taste zum Neustart drücken. 'q' zum beenden.") == "q":
        break




