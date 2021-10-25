def pathExist(m):
    rows , columns = len(m) ,len(m[0])
    x , y , fx , fy , c = 0 , 0 , rows-1 , columns-1 , 2
    for j in range(columns): #Prints the Given Maze
        for a in m:
            print(" ", a[j] , end=' ')
        print()
    print('\n\n')
    while True: #Check for the Solution
        pUp , pDown , pLeft , pRight = 0,0,0,0
        if x != 0:
            pLeft = m[x-1][y]
        if x != fx:
            pRight = m[x+1][y]
        if y != 0:
            pUp = m[x][y-1]
        if y != fy:
            pDown = m[x][y+1]
        possiblePaths = [pUp , pDown , pLeft , pRight].count(1) #check for number of possible paths
        if x == fx and y == fy: #Check if final State is achieved
            print('Solvable')
            for j in range(len(m)): #Route Recreate
                for a in range(len(m[j])):
                    if m[j][a] == 1:
                        m[j][a] = 0
                    if m[j][a] >= 2:
                        m[j][a] = 'S'
                m[0][0] = 'S'
            for j in range(columns): #Prints solution Maze
                for a in m:
                    print(" ", a[j] , end=' ')
                print()
            break
        if possiblePaths == 0 and x==0 and y == 0: #Check for unsolvable
            print("Unsolvable")
            break
        m[0][0] = 0
        if possiblePaths == 0:
            for j in range(len(m)): #Soft Reset when encountering no way home
                for a in range(len(m[j])):
                    if m[j][a] == c:
                        m[j][a] = 0
                    if m[j][a] >= 2 and m[j][a]<c:
                        m[j][a] = 1
            x , y , c = 0 , 0 ,2
        else: #Move across the paths in a preferential order
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
            else: #make exception points for crossroads and nested Crossroads
                c+=1
                m[x][y] = c
        #input()     # Input() to make the states iterate one by one
pathExist([ [1,1,1,1,1] , [0,0,1,0,1] , [0,0,1,0,1] , [0,0,0,0,1] , [1,1,1,1,1] , [1,0,0,1,0] , [1,0,1,1,1] ])
