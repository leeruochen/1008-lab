def isValid(c, r, chessboard):
    for i in range(r): # check columns
        if chessboard[i][c] == 1:
            return False
    
    i = r - 1 # move up
    j = c - 1 # move left
    while i >= 0 and j >= 0: # check upper left diagonal
        if chessboard[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = r - 1 # move up
    j = c + 1 # move right
    while i >= 0 and j < len(chessboard): # check upper right diagonal
        if chessboard[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def printSolution(chessboard):
    print("\n")
    for row in range(len(chessboard)):
        print(chessboard[row])

def putAQueen(r, chessboard):
    N = len(chessboard)
    for c in range(N): # iterate through columns
        if isValid(c, r, chessboard):
            chessboard[r][c] = 1
            if (r < N - 1):
                putAQueen(r + 1, chessboard)
            else:
                printSolution(chessboard)
                exit()
            chessboard[r][c] = 0

N = 8
chessboard = [[0 for i in range(N)] for j in range(N)]
putAQueen(0, chessboard)