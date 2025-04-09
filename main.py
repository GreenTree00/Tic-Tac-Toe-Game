from gameboard import GameBoard

gameboard = GameBoard()

game_on = True

turn = 0

while game_on:
    play_game = input("Would you like to play Tic Tac Toe? 'y' to play and 'n' to stop.\n").lower()
    if play_game == "y":
        gameboard.board()
        while game_on:
            if turn % 2 == 0:
                player = "Player X"
                sign = "X"
            else:
                player = "Player O"
                sign = "O"
            move = input(f"{player}, please select a place on the board.").upper()
            if gameboard.place_sign((move), sign) == False:
                print("Please select an open spot")
            else:
                win = gameboard.checkwin(letter=sign)
                if win:
                    game_on = False
                turn += 1
                if turn == 9 and win != True:
                    game_on = False
                    print("Game over Tie")

    if play_game == 'n':
        game_on = False
    else:
        if game_on:
            print(f"You typed '{play_game}' please enter a valid letter.\n")
