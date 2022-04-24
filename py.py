
globalComp, globalPlay = '', ''
moves = 0
def drawBoard(board):               #fungsi untuk mengambar board
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

def inputPlayerLetter():            #fungsi untuk memilih simbol player
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def playAgain():                #fungsi untuk memilih jika ingin main lagi atau tidak
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):  #fungsi untuk melakukan gerakkan
    board[move] = letter

def isWinner(bo, le):          #fungsi untuk mengecek jika ada yang menang
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def getBoardCopy(board):       #fungsi untuk mengcopy board pada saat ini
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):  #fungsi untuk mengecek jika cell sudah diambil
    return board[move] == ' '
#9 8 7 6 5 4 3 2 1
def getPlayerMove(board): #fungsi untuk memilih pergerakkan untuk player
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def checkPossibleMoves(board):  #fungsi agar komputer dapat melihat pergerakkan
    possibleMoves = []          # yg dapat dilakukan
    for i in range(1,10):
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return possibleMoves
    else:
        return None

def maxVal(board,currTurn,alpha,beta): #fungsi untuk memaksimalkan keunggulan komputer
 
    if isWinner(board, globalPlay):    # jika gerakkan membuat player menang
        return -1                       # abaikan
    elif isWinner(board, globalComp):  # jika gerakkan membuat komputer menang
        return 1                     # prioritaskan
    elif isBoardFull(board):           # jika gerakkan membuat seri
        return 0                      # prioritaskan jika gerakkan lain menyebabkan kekalahan
    
    if currTurn== 'X':
        nextTurn = 'O'
    else:
        nextTurn = 'X'

    possibleMoves = checkPossibleMoves(board)   #lihat gerakkan yg dapat komputer lakukan
    score = -100000
    global moves
    for i in possibleMoves:            #cari gerakkan yg maksimal diantara gerakkan 
        moves = moves +1               # yg meminimalkan keunggulan komputer
        copy = getBoardCopy(board)
        makeMove(copy,currTurn,i)
        score = max(score,minVal(copy,nextTurn,alpha,beta))
        if score >= beta:
            return score
        alpha = max(alpha,score)
    return score

def minVal(board,currTurn,alpha,beta):  #fungsi untuk meminimalkan keunggulan player

    if isWinner(board, globalPlay):    # jika gerakkan membuat player menang
        return -1                       # abaikan
    elif isWinner(board, globalComp):  # jika gerakkan membuat komputer menang
        return 1                    # prioritaskan
    elif isBoardFull(board):           # jika gerakkan membuat seri
        return 0                      # prioritaskan jika gerakkan lain menyebabkan kekalahan
  
    if currTurn== 'X':
        nextTurn = 'O'
    else:
        nextTurn = 'X'

    possibleMoves = checkPossibleMoves(board) #lihat gerakkan yg dapat player lakukan
    score = 100000
    global moves
    for i in possibleMoves:    # cari gerakkan yg minimal diantara gerakkan
        moves = moves +1       # yg memaksimalkan keunggulan player
        copy = getBoardCopy(board)
        makeMove(copy,currTurn,i)
        score = min(score, maxVal(copy,nextTurn,alpha,beta))
        if score <= alpha:
            return score
        beta = min(beta,score)
    return score

def getComputerMove(board, computerLetter): # fungsi agar komputer dapat bergerak

    if computerLetter== 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    possibleMoves = checkPossibleMoves(board) # lihat gerakkan yg dapat dilakukan komputer
    alpha = -100000
    beta = 100000
    score = -100000
    global moves
    for i in possibleMoves:  # cari gerakkan yg optimal dengan minmax
        moves = moves + 1
        copy = getBoardCopy(board)
        makeMove(copy,computerLetter,i)
        s = minVal(copy,playerLetter,alpha,beta)
        if s > alpha:
            score = s
            move = i
        alpha = max(alpha,score)
    
    return move

def isBoardFull(board):        # fungsi untuk mencek jika seri/ board penuh
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!') #fungsi main

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    globalPlay, globalComp = playerLetter, computerLetter
    if playerLetter == 'X': #player terlebih dahulu
        turn = 'player' 
    else: #computer terlebih dahulu
        turn = 'computer'
    print('The ' + turn + ' will go first.')    
    gameIsPlaying = True
    while gameIsPlaying:                    #jika game masih berjalan
        moves = 0
        if turn == 'player':
            drawBoard(theBoard)            #gambarkan board
            move = getPlayerMove(theBoard)  #tanyakan gerakkan player
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):    # cek jika player menang 
                drawBoard(theBoard)                 # setelah melakukan gerakkan
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):   # cek jika seri setelah melakukan gerakkan
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'   # jika belum ada yang menang komputer boleh bergerak

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter): # cek jika komputer menang setelah 
                drawBoard(theBoard)                # melakukan gerakkan
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):   # cek jika seri setelah melakukan gerakkan
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player' # jika belum ada yang menang komputer boleh bergerak
            print('Moves explored: ', moves)

    if not playAgain():
        break