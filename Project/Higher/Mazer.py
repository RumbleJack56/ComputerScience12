def pathExist(m):
    #Basic For the Maze
    c = 2
    rows = len(m)
    columns = len(m[0])

    #Initialize Start and End Points
    x , y , fx , fy = 0 , 0 , rows-1 , columns-1
    while True:


        pUp , pDown , pLeft , pRight = 0,0,0,0
        #Check around Start Point
        if x != 0:
            pLeft = m[x-1][y]
        if x != fx:
            pRight = m[x+1][y]
        if y != 0:
            pUp = m[x][y-1]
        if y != fy:
            pDown = m[x][y+1]


        possiblePaths = [pUp , pDown , pLeft , pRight].count(1)


        if x == fx and y == fy:
            print('Solvable')
            break

        if possiblePaths == 0 and x==0 and y == 0:
            print("Unsolvable")
            break

        #Print Maze
        for j in range(columns):
            for a in m:
                print(" ", a[j] , end=' ')
            print()
        print('\n\n')
        m[0][0] = 0


        if possiblePaths == 0:
            #Soft Reset
            for j in range(len(m)):
                for a in range(len(m[j])):
                    if m[j][a] == c:
                        m[j][a] = 0
                    if m[j][a] >= 2 and m[j][a]<c:
                        m[j][a] = 1
            x , y , c = 0 , 0 ,2
        else:
            if pDown == 1:
                y+=1
            elif pUp ==1:
                y-=1
            elif pLeft == 1:
                x-=1
            elif pRight == 1:
                x+=1

            if possiblePaths == 1:
                m[x][y] = 2
            else:
                c+=1
                m[x][y] = c
        #input()


pathExist([[1,1,1,1,1], [0,0,1,0,1] , [0,0,1,0,1] , [0,0,0,0,1] , [1,1,1,1,1] , [1,0,0,1,0] , [1,0,1,1,1]])
