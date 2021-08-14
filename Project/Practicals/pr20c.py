n=int(input("Number: "))
startPoint=8
for j in range(1,n+1):
    for num in range(1,j+1):
        temp=startPoint - 2*num + 2
        print(temp,end=' ')
    print('')
