
# Ratespiel
# Konsolenratespiel mit Fehlercheck


def pruef_rate(rate, antwort):

    global punkte
    versuche = 0
    game_running = True
    while game_running and versuche < 3:
        if rate.lower() == antwort.lower():
            print("Das war richtig. ")
            punkte += 1
            game_running = False
        elif versuche < 2:
            rate = input("Das war falsch, versuche es erneut. ")
            versuche += 1

        else:
            print("Die richtige Antwort war: " + antwort)
            game_running = False


punkte = 0
print()
print(" - Ratespiel - ")
print()


frage_1 = input("Was ist die beste Programmiersprache? ")
pruef_rate(frage_1, "Python")
frage_2 = input("Wie ist der Vorname von Python? ")
pruef_rate(frage_2, "Monty")
frage_3 = input("Wie viele Mitglieder hatte die Komikergruppe MP? ")
pruef_rate(frage_3, "6")
frage_4 = input("Wie viele offizielle Computerspiele existieren über Monty Python? ")
pruef_rate(frage_4, "5")
frage_5 = input("Der Titel eines MP Films war: Das Leben des ... ? ")
pruef_rate(frage_5, "Brian")
frage_6 = input("Der Titel eines MP Films war: Die Ritter der ... ? ")
pruef_rate(frage_6, "Kokosnuß")
frage_7 = input("Wie viele Musicals existieren zu MP? ")
pruef_rate(frage_7, "3")
frage_8 = input("An welcher Universität studierte Eric Idle? ")
pruef_rate(frage_8, "Cambridge")
frage_9 = input("In welchem Jahr erschien Das Leben des Brian? ")
pruef_rate(frage_9, "1979")
frage_10 = input("Wie hieß die Firma, die Das Leben des Brian produziert hat? ")
pruef_rate(frage_10, "HandMade Films")




print("-" * 30)
print("Du hast " + str(punkte) + " Punkte geschafft.")
print("-" * 30)
input("Beliebige Taste zum beenden drücken.")









