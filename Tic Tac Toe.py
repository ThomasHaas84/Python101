
# Tic Tac Toe
# TTT Konsolenspiel


import time

# Spielfeld
print()
print("Tic Tac Toe")
print()
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

# Falls das Spiel noch läuft
game_still_going = True

# Wer hat gewonnen?
winner = None

# Wer ist an der Reihe?
# Spieler 'X' fängt an
current_player = "X"


def display_board():
    print(board[6] + " | " + board[7] + " | " + board[8])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[0] + " | " + board[1] + " | " + board[2])


def play_game():
    display_board()

    while game_still_going:

        # Spielzug
        handle_turn(current_player)

        # Läuft das Spiel noch?
        check_if_game_over()

        # Spielerwechsel
        flip_player()

    # Das Spiel endet
    if winner == "X" or winner == "O":
       print()
       print(winner + " hat gewonnen!")
    elif winner == None:
        print()
        print("Unentschieden.")
    time.sleep(2)
    print(input("Beliebige Taste zum beenden drücken."))


def handle_turn(player):
    print()
    print(player + " ist an der Reihe.")
    position = input("Wähle eine Position von 1 bis 9: ")
    print()
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9",]:
          position = input("Eine Zahl von 1 bis 9: ")

        position = int(position) - 1

        if board[position] == "-":
           valid = True
        else:
           print("Hier ist schon besetzt.")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    # Zeile überprüfen
    row_winner = check_rows()
    # Spalte überprüfen
    column_winner = check_columns()
    # Diagonale überprüfen
    diagonal_winner = check_diagonals()
    if row_winner:
        # Gewinner Zeile
        winner = row_winner
    elif column_winner:
        # Gewinner Spalte
        winner = column_winner
    elif diagonal_winner:
        # Gewinner Diagonale
        winner = diagonal_winner
    else:
        # Es gibt noch keinen Gewinner
        winner = None
    return


def check_rows():

    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Sieger ermitteln ( X oder O )
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():

    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Sieger ermitteln ( X oder O )
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():

    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    if diagonals_1 or diagonals_2:
        game_still_going = False

    # Sieger ermitteln ( X oder O )
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()



