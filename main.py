import random

# Tic Tac Toe game in python

board = [' ' for _ in range(10)]  # Board initialization


# Insert value into array
def insert_letter(letter, pos, board_data):
    board_data[pos] = letter
    return board_data


# Check if space is free
def space_is_free(pos, board_data):
    return board_data[pos] == ' '


# Print the board with available positions
def print_board(board_data):
    print('   |   |')
    for i in range(1, 10, 3):
        print(' ' + (board_data[i] if board_data[i] != ' ' else str(i)) +
              ' | ' + (board_data[i + 1] if board_data[i + 1] != ' ' else str(i + 1)) +
              ' | ' + (board_data[i + 2] if board_data[i + 2] != ' ' else str(i + 2)))
        if i < 7:
            print('-----------')
    print('   |   |')


# Check if there is a winner
def is_winner(board_data, le):
    return (board_data[7] == le and board_data[8] == le and board_data[9] == le) or \
        (board_data[4] == le and board_data[5] == le and board_data[6] == le) or \
        (board_data[1] == le and board_data[2] == le and board_data[3] == le) or \
        (board_data[1] == le and board_data[4] == le and board_data[7] == le) or \
        (board_data[2] == le and board_data[5] == le and board_data[8] == le) or \
        (board_data[3] == le and board_data[6] == le and board_data[9] == le) or \
        (board_data[1] == le and board_data[5] == le and board_data[9] == le) or \
        (board_data[3] == le and board_data[5] == le and board_data[7] == le)


# Player move
def player_move(board_data):
    while True:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move, board_data):
                    board_data = insert_letter('X', move, board_data)
                    break
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range 1-9!')
        except ValueError:
            print('Please type a valid number!')
    return board_data


# Computer move
def comp_move(board_data):
    possible_moves = [x for x, letter in enumerate(board_data) if letter == ' ' and x != 0]
    move = 0

    # Check for winning or blocking moves
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board_data[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    # Check for available corners
    corners_open = [i for i in possible_moves if i in [1, 3, 7, 9]]
    if corners_open:
        move = select_random(corners_open)
        return move

    # Check if the center is available
    if 5 in possible_moves:
        return 5

    # Check for available edges
    edges_open = [i for i in possible_moves if i in [2, 4, 6, 8]]
    if edges_open:
        move = select_random(edges_open)
        return move

    return move


# Select random space
def select_random(li):
    return random.choice(li)


# Check if board is full
def is_board_full(board_data):
    return board_data.count(' ') == 1


# The main game
def game():
    print('Welcome to Tic Tac Toe!')

    # Instructions for the player
    print("""
    How to play Tic Tac Toe:

    1. The game is played on a 3x3 grid. You will play as 'X', and the computer plays as 'O'.
    2. The positions on the board are numbered from 1 to 9, starting from the top left, going across each row.
       Here is the board layout for reference:

        1 | 2 | 3
       -----------
        4 | 5 | 6
       -----------
        7 | 8 | 9

    3. To make your move, input the number (1-9) corresponding to the position where you want to place your 'X'.
    4. The computer will then make its move as 'O'.
    5. The first player to align 3 of their marks (vertically, horizontally, or diagonally) wins.
    6. The game ends in a tie if all positions are filled and no one wins.
    """)

    board_data = board[:]  # Copy of the board to work with inside the game
    print_board(board_data)

    while not is_board_full(board_data):
        if not is_winner(board_data, 'O'):
            board_data = player_move(board_data)
            print_board(board_data)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not is_winner(board_data, 'X'):
            move = comp_move(board_data)
            if move == 0:
                print('Tie Game!')
            else:
                board_data = insert_letter('O', move, board_data)
                print(f'Computer placed an \'O\' in position {move}:')
                print_board(board_data)
        else:
            print('X\'s won this time! Good job!')
            break

    if is_board_full(board_data):
        print('Tie Game!')


if __name__ == '__main__':
    game()  # Start the first game

    # Ask if the player wants to play again after the game ends
    while True:
        answer = input('Do you want to play again? (Y/N): ').lower()
        if answer in ['y', 'yes']:
            board = [' ' for _ in range(10)]  # Reset the board
            print('-----------------------------------')
            game()  # Start a new game
        else:
            break  # Exit the game
