
# Zahlenraten
# Eine Zufallszahl erraten


import random


class GuessNumber:
    def __init__(self, mn=1, bereich=100):
        self.number = random.randint(mn, bereich)
        self.guesses = 0
        self.min = mn
        self.max = bereich


    def get_guess(self):
        print("-" * 40)
        guess = input(f"Zahl im Bereich von {self.min} und {self.max} eingeben: ")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Bitte eine ganze Zahl im Auswahlbereich eingeben.")
            return self.get_guess()


    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False
        return self.min <= number <= self.max


    def play(self):
        while True:
            self.guesses += 1
            guess = self.get_guess()

            if guess < self.number:
                print("Die Zahl ist höher.")
            elif guess > self.number:
                print("Die Zahl ist niedriger.")
            else:   # Die Zahl wurde erraten
                break

        print(f"\nDu hast die Zahl erraten. \nEs war die '{self.number}'. \nDu hast {self.guesses} Versuche gebraucht.\n")


def new_round():
    while True:
        print()
        print("-" * 40)
        print("-Zahlenraten-")
        print("-" * 40)

        while True:
            bereich = (input("Bereich eingeben: "))
            try:
                bereich = int(bereich)
            except:
                print("Bitte nur ganze Zahlen eingeben.")
            else:
                break
        game = GuessNumber(1, bereich)
        game.play()
        if input("\nZum Beenden 'q', beliebige Taste für Neustart.") == "q":
            break
        else:
            pass


new_round()

