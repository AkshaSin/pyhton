#Tic Tac Toe game in python
board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('     |      |      |')
    print(' ' + board[1] + '   | ' + board[2] + '    | ' + board[3] + '    | '+board[4])
    print('     |      |      |')
    print('-----------------------------')
    print('     |      |      |')
    print(' ' + board[5] + '   | ' + board[6] + '    | ' + board[7]+ '    | '+board[8])
    print('     |      |      |')
    print('-----------------------------')
    print('     |      |      |')
    print(' ' + board[9] + '   | ' + board[10] + '    | ' + board[11]+ '    | '+board[12])
    print('     |      |      |')
    print('------------------------------')
    print('     |      |      |')
    print(' ' + board[13] + '   | ' + board[14] + '    | ' + board[15]+ '    | '+board[16])
    print('     |      |      |')



def isWinner(bo, le):
    return (bo[13] == le and bo[14] == le and bo[15] == le and bo[15] == le) or \
           (bo[9] == le and bo[10] == le and bo[11] == le and bo[12] == le) or\
           (bo[5] == le and bo[6] == le and bo[7] == le and bo[8] == le) or\
           (bo[1] == le and bo[2] == le and bo[3] == le and bo[4] == le) or\
           (bo[1] == le and bo[5] == le and bo[9] == le and bo[13] == le) or\
           (bo[2] == le and bo[6] == le and bo[10] == le and bo[14] == le) or\
           (bo[3] == le and bo[7] == le and bo[11] == le and bo[15] == le) or\
           (bo[4] == le and bo[8] == le and bo[12] == le and bo[16] == le) or\
           (bo[1] == le and bo[6] == le and bo[11] == le and bo[16] == le) or \
           (bo[4] == le and bo[7] == le and bo[10] == le and bo[13] == le)

def PlayerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-16): ')
        try:
            move = int(move)
            if move > 0 and move < 17:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def CompMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,4,13,16]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if [6,7,10,11] in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,3,5,9,8,12,14,15]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            PlayerMove()
            printBoard(board)
        else:
            print('Sorry,Computer won this time, better luck next time!')
            break

        if not(isWinner(board, 'X')):
            move = CompMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('You won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(17)]
        print('-----------------------------------')
        main()
    else:
        break
