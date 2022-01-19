#Checks the x axis for already given values

def checkRow(mtrx , x , y):
    pt = mtrx[y][x]
    return [k for k in (1,2,3,4,5,6,7,8,9) if k not in mtrx[y] ]




#Check for Values in column

def checkColumn(mtrx , x , y):
    pt = mtrx[y][x]
    vals = [p[x] for p in mtrx] 
    return [k for k in (1,2,3,4,5,6,7,8,9) if k not in vals]



#Check for values in respective 3x3

def check3x3(mtrx , x , y):
    xCheck , yCheck , pt = 0 , 0 ,mtrx[y][x]
    #Finds the 3x3 box of the point
    if x in (0,1,2): xCheck = (0,1,2)
    elif x in (3,4,5): xCheck = (3,4,5)
    else: xCheck = (6,7,8)

    if y in (0,1,2): yCheck = (0,1,2)
    elif y in (3,4,5): yCheck = (3,4,5)
    else: yCheck = (6,7,8)

    vals = [mtrx[k][h] for k in yCheck for h in xCheck]
    return [k for k in (1,2,3,4,5,6,7,8,9) if k not in vals]



def enterVal(doku, x, y, val):
    doku[y-1][x-1] = val

def printSudoku(doku):
    for j in doku:
        print(j)



