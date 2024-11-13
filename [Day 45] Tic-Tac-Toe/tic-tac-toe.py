import random 

global board
board = []

def init_game():
    global board
    board = [" " for _ in range(9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_turn():
    while True:
        try:
            player_choice = int(input("Enter a position (1-9): ")) - 1
            if board[player_choice] == " ":
                board[player_choice] = "O"
                break
            else:
                print("That position is already taken.")
        except (ValueError, IndexError):
            print("Please enter a value between 1 and 9.")

    pass

def ai_turn():
    empty = [i for i,x in enumerate(board) if x == " "]
    ai_choice = random.choice(empty)
    board[ai_choice] = "X"

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return board[combination[0]]
    return None

def game_loop():
    turn = 0
    while True:
        print_board()
        if turn % 2 == 0:
            player_turn()
        else:
            ai_turn()

        winner = check_winner()
        if winner:
            print_board()
            print(f"{winner} wins!")
            break

        if " " not in board:
            print_board()
            print("It's a draw!")
            break

        turn += 1

    pass

def game_start():
    while True:
        init_game()
        game_loop()

        print("Do you want to play again: Type Y to play again")
        if input(">>> ") == "Y":
            continue
        else:
            break

game_start()


