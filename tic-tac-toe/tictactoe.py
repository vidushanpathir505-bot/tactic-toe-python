#TIC-TAC-TOE GAME

import random

board = ['_','_','_',
         '_','_','_',
         '_','_','_',]

BOT = "O"

def game_board(board):          #print the game board

    print( board[0], '|' ,board[1], '|' ,board[2])
    print("---------")
    print( board[3], '|' ,board[4], '|' ,board[5])
    print("---------")
    print( board[6], '|' ,board[7], '|' ,board[8])
    

def choose_winner(board):
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),   
        (0,3,6), (1,4,7), (2,5,8),   
        (0,4,8), (2,4,6)             
    ]

    # Check for a winner
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] != '_':
            print('🎉-----🎉-----🎉')
            print(f"---🎉{board[a]} YOU WON🎉---")   
            print('🎉-----🎉-----🎉')
            print()
            return True
        

    # Check for draw (no spaces left)
    if '_' not in board:
        print('-----😓-----')
        print("    Draw ☹     ")
        print('-----😓-----')
        print()
        return True

    # No winner yet, game still ongoing
    return None

def game_bot(board):         #game bot

    if board[4] == '_':
        board[4] = BOT
        return

    empty = [i for i in range(9) if board[i] == "_"]
    board[random.choice(empty)] = BOT

def board_cleaner(board):           #clean the board to play new round

    for i in range(9):

        if  board[i] == 'X' or board[i] == 'O':
            board[i] = '_'

def show_messages(prompt):            #show clearly player to error messages
    print()
    print(prompt)
    print()

def main(board):

    print('|---------||---------|')
    print("WELCOME TO TIC TAC TOE")
    print('|---------||---------|')
    print()
    print('--BOARD--')
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")
    print()

    while True:
        match input("1. 1 VS 1\n2. Game BOT\n3.Exit\n__:"):
            case "1":
                player1 = "X"
                player2 = "O"

                while True:

                    try:
                        move1 = int(input('Enter position (1-9): ')) - 1

                    except ValueError:          #Checking for value error
                        show_messages('Enter Valid Number')
                        continue   

                    if move1 < 0 or move1 > 9:          #Checking for out of range indexeses
                        show_messages('Enter Valid Number')
                        continue

                    if board[move1] != '_':
                        show_messages('Position already taken')
                        continue

                    board[move1] = player1

                    game_board(board)

                    winner = choose_winner(board)
                    if winner:
                        board_cleaner(board)
                        break

                    try:
                        move2 = int(input('Enter position (1-9): ')) - 1

                    except ValueError:          #Checking for value error
                        show_messages('Enter Valid Number')       
                        continue   

                    if move2 < 0 or move2 > 9:          #Checking for out of range indexeses
                        show_messages('Enter Valid Number')
                        continue

                    if board[move2] != '_':
                        show_messages('Position already taken')
                        continue

                    board[move2] = player2

                    game_board(board)

                    winner = choose_winner(board)
                    if winner:
                        board_cleaner(board)
                        break
            
            case "2":

                while True:

                    player1 = "X"

                    try:
                        move1 = int(input("Enter your move (1-9): ")) - 1

                    except ValueError:          #Checking for value error
                        show_messages('Enter Valid Number')     
                        continue   

                    if move1 < 0 or move1 > 9:          #Checking for out of range indexeses
                        show_messages('Enter Valid Number')
                        continue   

                    if board[move1] != '_':
                        show_messages('Position already taken')
                        continue

                    board[move1] = player1

                    winner = choose_winner(board)
                    if winner:
                        board_cleaner(board)
                        break

                    game_bot(board)

                    game_board(board)

                    winner = choose_winner(board)
                    if winner:
                        board_cleaner(board)
                        break

            case "3":
                show_messages('🙏Thanks for playing!🙏')
                break      

            case _:
                show_messages('🙃Invalid input🙃')    

if __name__ == '__main__':
    main(board)




        


