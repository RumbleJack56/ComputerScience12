#Self Built Function Library
from dokuFunc import *

def totalPossibleVals(mtrx,x,y):
    x=x-1
    y=y-1
    val = []
    for a in range(1,10):
        if a in checkRow(mtrx,x,y):
            if a in checkColumn(mtrx,x,y):
                if a in check3x3(mtrx,x,y):
                    val.append(a)
    return val





doku = [[0 for __ in range(9)] for _ in range(9)]
printSudoku(doku)
print()
enterVal(doku,7,1,2)
enterVal(doku,2,2,8)
enterVal(doku,6,2,7)
enterVal(doku,8,2,9)
enterVal(doku,1,3,6)
enterVal(doku,3,3,2)
enterVal(doku,7,3,5)
enterVal(doku,2,4,7)
enterVal(doku,5,4,6)
enterVal(doku,4,5,9)
enterVal(doku,6,5,1)
enterVal(doku,5,6,2)
enterVal(doku,8,6,4)
enterVal(doku,3,7,5)
enterVal(doku,7,7,6)
enterVal(doku,9,7,3)
enterVal(doku,2,8,9)
enterVal(doku,4,8,4)
enterVal(doku,8,8,7)
enterVal(doku,3,9,6)



posVals = [ [[] for _ in range(9)] for __ in range(9) ] 

for m in range(1,10):
    for n in range(1,10):
        if doku[n-1][m-1] == 0:
            posVals[n-1][m-1] = totalPossibleVals(doku,m,n)

for j in posVals:
    for k in j:
        print(k)
    print()

for a in range(9):
    for b in range(9):
        if len(posVals[b][a]) == 1
            doku[b][a] = posVals[b][a][0]
printSudoku(doku)

