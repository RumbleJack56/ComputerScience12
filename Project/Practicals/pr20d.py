n=8
for j in range(n,0,-1):
    for sp in range(1,n+1-j):
        print(" ", end='')
    for num in range(1,j+1):
        print("$ ",end='')
    print('')
