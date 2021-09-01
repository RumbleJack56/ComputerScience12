def pyramid(n):
    for sp in range(1 ,n-j+1):
        print(" ",end='')
    for num in range(j,0,-1):
        print("& ",end="")
    print('')
count=6
for j in range(count,0,-1):
    pyramid(count)
for j in range(1,count+1):
    pyramid(count)
