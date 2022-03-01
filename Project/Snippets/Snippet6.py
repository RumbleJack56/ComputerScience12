from rich import print
class Sudoku:
    def __init__(self):
        self.grid = [[' ' for x in range(9)] for y in range(9)]
        self.solved = False
        self.given = self.grid.copy()

    def isValid(self, x, y, val):
        if val in [row[x] for row in self.grid]: return 0
        if val in self.grid[y]: return 0
        xn , yn = x - x%3 , y - y%3
        for i in range(xn, xn+3):
            for j in range(yn, yn+3):
                if self.grid[i][j] == val:
                    return 0
        return 1

    def takeInput(self, x , y , val):
        self.grid[y][x] = val

    def solve(self):
        self.given = self.grid.copy()
        for one in range(9):
            for two in range(9):
                if self.grid[one][two] == ' ':
                    for pVal in range(1,10):
                        if self.isValid(one,two,pVal):
                            self.grid[one][two]=pVal
                            isSolved = self.solve()
                            if isSolved==True:
                                return True
                            else:
                                self.grid[one][two]=' '
                    return False
        return True

board = Sudoku()

print("""  Enter your values in following format:
  [blue]x y v[/blue]
  [red]x[/red] is the x coordinate from left
  [red]y[/red] is the y coordinate from top
  [red]v[/red] is number in that position
  All values are between 1 and 9
  Type [red]'solve'[/red] to solve \n""")

while True:
    inp = input("Enter Values: ").split()
    if inp[0].lower()=='solve': break
    if len(inp)==3 and int(inp[0]) in range(9) and int(inp[1]) in range(9) and int(inp[2]) in range(1,10):
        if board.isValid(int(inp[0]),int(inp[1]),int(inp[2])):
            board.takeInput(int(inp[0]),int(inp[1]),int(inp[2]))
            print(board.grid)
            continue
    print("Invalid Input Try Again")
    
board.solve()
print(board.grid)