import random


def full_board():
    board_full = 0
    for x in board:
        if x != ' ':
            board_full += 1
    if board_full == 9:
        print("It's a draw. No losers, no winners! ;-)")
        return True


def winner(char):
    winning_row = [char, char, char]

    # Check horizontal lines
    if all(elem in winning_row for elem in board[0:3]):
        return True
    elif all(elem in winning_row for elem in board[3:6]):
        return True
    elif all(elem in winning_row for elem in board[6:9]):
        return True

    # Check vertical lines
    elif all(elem in winning_row for elem in board[0:9:3]):
        return True
    elif all(elem in winning_row for elem in board[1:10:3]):
        return True
    elif all(elem in winning_row for elem in board[2:11:3]):
        return True

    # Check diagonal lines
    elif all(elem in winning_row for elem in board[0:10:4]):
        return True
    elif all(elem in winning_row for elem in board[2:8:2]):
        return True


def check_board(move):
    if board[move - 1] == 'X' or board[move - 1] == 'O':
        print('That position is already taken, try again.')
        return False
    else:
        return True


def update_board(move, char):
    if move:
        board[move - 1] = char
        print(f'{board[6:9]}\n{board[3:6]}\n{board[0:3]}')


def player_move():
    while True:
        try:
            move = int(input('What position do you want to play? Choose between 1-9:'))
        except ValueError:
            print('Invalid input. Choose a number between 1 and 9.')
            continue
        try:
            if check_board(move):
                return move
        except IndexError:
            print('Invalid input. Choose a number between 1 and 9.')
            continue


def com_move():
    com_list = []
    for n in range(len(board)):
        if board[n] == ' ':
            com_list.append(n)
    move = random.choice(com_list) + 1
    print(f'Computer makes his move... {move}')
    return move


def tic_tac_toe():
    while True:
        player = player_move()
        update_board(player, 'X')
        if winner('X'):
            print('You WON! :-D')
            break
        if full_board():
            break
        com = com_move()
        update_board(com, 'O')
        if winner('O'):
            print('Computer won this time. :-(')
            break


while True:
    board = [' ' for num in range(1, 10)]
    board_with_positions = [str(num) for num in range(1, 10)]
    print(f'{board_with_positions[6:9]}\n{board_with_positions[3:6]}\n{board_with_positions[0:3]}')
    tic_tac_toe()
    if input("Do you want to play again? Type 'y' or 'n': ").upper() == 'N':
        break
