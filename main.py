# Tic Tac Toe game in python

board = [' ' for x in range(10)]

# Insert value into array
def insertLetter(letter, pos):
    board[pos] = letter

# Check if space is open
def spaceIsFree(pos):
    return board[pos] == ' '

# Print the board
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# Check if there is a winner
def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

# Player move
def player_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# Computer move
def comp_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if is_winner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = select_random(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = select_random(edgesOpen)

    return move

# Select random space
def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# Check if board is full
def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# The main game
def game():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not (is_board_full(board)):
        if not (is_winner(board, 'O')):
            player_move()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (is_winner(board, 'X')):
            move = comp_move()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if is_board_full(board):
        print('Tie Game!')



if __name__ == '__main__':
    while True:
        answer = input('Do you want to play again? (Y/N): ')
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            board = [' ' for x in range(10)]
            print('-----------------------------------')
            game()
        else:
            break