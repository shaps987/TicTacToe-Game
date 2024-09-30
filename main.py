import numpy as np

TURN_NUMBER = 0

PLAYER_X_WIN = False
PLAYER_O_WIN = False

COLUMN_RESPONSES = {"left":0, "center":1, "right":2}
ROW_RESPONSES = {"top":0, "middle":1, "bottom":2}

board = np.array([[" "," "," "],
                 [" "," "," "],
                 [" "," "," "]])

print("Welcome to Tic-Tac-Toe!")
print("It's Player vs Player")
print(f"X goes first")

def player_turn(player_letter):
    global TURN_NUMBER

    TURN_NUMBER += 1

    row = input(f"{player_letter}, what row would you like to place your piece in? (top, middle, or bottom) ").lower()
    while row not in ROW_RESPONSES:
        print("Invalid Input")
        row = input(f"{player_letter}, what row would you like to place your piece in? (top, middle, or bottom) ").lower()
    
    column = input(f"{player_letter}, what column would you like to place your piece in? (left, center or right) ").lower()
    while column not in COLUMN_RESPONSES:
        print("Invalid Input")
        column = input(f"{player_letter}, what column would you like to place your piece in? (left, center or right) ").lower()
    
    while board[ROW_RESPONSES[row]][COLUMN_RESPONSES[column]] != " ":
        print("That box is already taken")
        print("Please pick again")

        row = input(f"{player_letter}, what row would you like to place your piece in? (top, middle, or bottom) ").lower()
        while row not in ROW_RESPONSES:
            print("Invalid Input")
            row = input(f"{player_letter}, what row would you like to place your piece in? (top, middle, or bottom) ").lower()
        
        column = input(f"{player_letter}, what column would you like to place your piece in? (left, center or right) ").lower()
        while column not in COLUMN_RESPONSES:
            print("Invalid Input")
            column = input(f"{player_letter}, what column would you like to place your piece in? (left, center or right) ").lower()

    board[ROW_RESPONSES[row]][COLUMN_RESPONSES[column]] = player_letter
    
    display_board()

    check_for_win(player_letter)

def check_for_win(player):
    global PLAYER_X_WIN
    global PLAYER_O_WIN

    if board[0][0] == board[0][1] == board[0][2] == player or board[1][0] == board[1][1] == board[1][2] == player or board[2][0] == board[2][1] == board[2][2] == player or board[0][0] == board[1][0] == board[2][0] == player or board[0][1] == board[1][1] == board[2][1] == player or board[0][2] == board[1][2] == board[2][2] == player or board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        
        if player == "O":
            PLAYER_O_WIN = True
            print(f"O wins!")
        elif player == "X":
            PLAYER_X_WIN = True
            print(f"X wins!")
        print("Thank you for playing")

def display_board():
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print(f"-----")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print(f"-----")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")
    print("###########################################################")

while PLAYER_O_WIN == False and PLAYER_X_WIN == False and TURN_NUMBER <= 9:
    player_turn("X")
    if PLAYER_O_WIN == True or PLAYER_X_WIN == True or TURN_NUMBER > 9:
        break

    player_turn("O")
    if PLAYER_O_WIN == True or PLAYER_X_WIN == True or TURN_NUMBER > 9:
        break

if TURN_NUMBER == 9:
    print("Its a draw!")