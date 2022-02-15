tup = ((1,2,3) , (3,5,7) , (1,4,7))
print(tuple(sorted(tup, key =lambda x: x[1])))


tup = ((1,2,3) , (3,5,7) , (1,4,7))
tup = list(tup)
for x in range(len(tup)):
    for y in range(x+1,len(tup)):
        if tup[x][1] > tup[y][1]:
            tup[x] , tup[y] = tup[y] , tup[x]
print(tuple(tup))

