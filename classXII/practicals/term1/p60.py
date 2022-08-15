#15/08/22
#Random Matrix Diagonal Sum

import random
rMatrix = [[random.randrange(10,30) for a in range(3)] for b in range(3)]

for row in rMatrix:
    print(row)

#now we print diagonals
space = 3
sum = 0
for k in range(len(rMatrix)):
    print(("%"+str(space)+"s")%rMatrix[k][k])
    space+=3
    sum +=rMatrix[k][k]
print("\nSum: ",sum)
