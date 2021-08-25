n=4
startPoint = 2 * n
for j in range(1,n+1):
    print("  ", end='')
    for num in range(1,j+1):
        temp=startPoint - 2*num + 2
        print(temp,end=' ')
    print('')
