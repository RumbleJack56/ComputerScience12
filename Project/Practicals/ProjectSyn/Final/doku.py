# from rich import print
# myBoard = [[0, 4, 0, 7, 0, 0, 1, 3, 0],
#            [0, 0, 2, 0, 0, 0, 6, 0, 0],
#            [0, 0, 0, 4, 2, 0, 0, 0, 0],
#            [6, 0, 0, 0, 0, 2, 0, 0, 3],
#            [2, 3, 1, 0, 7, 0, 0, 8, 0],
#            [4, 0, 0, 3, 1, 0, 0, 0, 0],
#            [0, 7, 0, 0, 0, 8, 0, 0, 0],
#            [0, 0, 6, 0, 3, 0, 0, 0, 4],
#            [8, 9, 0, 0, 5, 0, 0, 0, 6]]
myBoard = [[' ' for _ in range(9)] for __ in range(9)]


def enterInput(board):

    print("""  Enter your values in following format:
     [blue]x y v[/blue]
     [red]x[/red] is the x coordinate from left
     [red]y[/red] is the y coordinate from top
     [red]v[/red] is number in that position
     All values are between 1 and 9
     Type [red]'solve'[/red] to solve \n""")
    c = 1
    while True:
        nStr = '1 2 3 4 5 6 7 8 9'
        while True:
            inp = input("   Enter Value "+str(c)+': ').split()
            if inp[0].lower() == 'solve':
                c = 0
                break
            try:
                if inp[0] in nStr and inp[1] in nStr and inp[2] in nStr:
                    inp = [ int(inp[0]) , int(inp[1]) , int(inp[2]) ]
                    putVal( board , inp[0] , inp[1] , inp[2])
                    break
            except: pass
            print("Invalid Input Try Again")
        if c==0:
            break
        c+=1

def putVal(board, x, y, v):
    board[y-1][x-1] = v
    for x in board:
        print('[',end='')
        for j in x:
            print(j,end=" ")
        print(']')

def isValid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    c_row = row - row%3
    c_col = col - col%3
    for i in range(c_row, c_row+3):
        for j in range(c_col, c_col+3):
            if board[i][j] == num:
                return False
    return True

def solveBoard(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ' ':
                for num in range(1,10):
                    if isValid(board, i, j, num):
                        board[i][j] = num
                        result = solveBoard(board)
                        if result == True:
                            return True
                        else:
                            board[i][j] = ' '
                return False
    return True

def printBoard(board):
    for line in board:
        print(line)
    input()
