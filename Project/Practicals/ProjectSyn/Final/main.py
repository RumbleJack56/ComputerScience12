###########################################################
#                      SUDOKU SOLVER                      #
###########################################################
 
import sys
from doku import *
try:
    import rich
except:
    print("Rich library not installed, Please install rich and then open")
    sys.exit()
from rich import print

print(
"""[blue]###########################################################
#[/blue]                      [bold red]SUDOKU SOLVER[/ bold red]                      [blue]#
###########################################################[/blue]""",end="\n\n")

print("[green]Welcome to Sudoku Solver [/green]")
print("""[green]This program allows you to solve the classic Sudoku Puzzle.
The Puzzle is famous with its 9x9 grid where no number repeats in its row, column or 3x3 square. [/green]\n""")

print("[blue]This project has been developed in two formats, one with GUI and another using the Console, please choose which would you prefer      \n1)GUI     \n2)Console[/blue]")
while True:
    global progType
    progType = input("Enter value[1 or 2]: ")
    if progType=='1' or progType=='2': 
        break
    print("[red]Invalid Input, Try Again[/red]")
if progType=='1':
    import doku_gui
if progType=='2':
    enterInput(myBoard)
    solveBoard(myBoard)
    printBoard(myBoard)