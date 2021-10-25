def pathExist(m):
rows = len(m)
columns = len(m[0])
x , y , fx , fy = 0 , 0 , rows-1 , columns-1
pUp , pDown , pLeft , pRight = 1,1,1,1
while True:
    p = m[x][y]
    if y!=0:
        pUp = m[x][y-1]
    if y!=4:
        pDown = m[x][y+1]
    if x!=rows-1:
        pLeft = m[x-1][y]
    if x!=columns-1:
        pDown = m[x+1][y]

    if pDown == 0:

        y+=1
