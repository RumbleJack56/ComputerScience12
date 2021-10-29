n = 4
for i in range(2,n+2):
    for j in range(10 - i):
        print(' ', end='')
    for j in range(i):
        print(" V",end='')
    for j in range(10 - 2*i):
        print(' ', end='')
    for j in range(i):
        print(" V",end='')
    print()
for i in range(n+1):
    print('      ', end='')
    for j in range(i):
        print("  ",end='')
    for j in range(2*(n-i)+1):
        print(" V", end='')
    print()
    