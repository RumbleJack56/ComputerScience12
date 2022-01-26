a = "H ;4 t akos"
out = ''
for j in a:
    if j.isspace():
        out+=j
    elif j.isdigit():
        out+=str(int(j) - 1)
    else:
        if j in 'aeiou':
            out+=j
        else:
            out+=chr( ord(j) + 1 )
print(out)


n = 4
for i in range(2,n+2):
    for j in range(10 - i):
        print('  ', end='')
    for j in range(i):
        print("  V",end='')
    for j in range(10 - 2*i):
        print(' ', end='')
    for j in range(i):
        print(" V",end='')
    print()
for i in range(n+1):
    print('         ', end='')
    for j in range(i):
        print("    ",end='')
    for j in range(2*(n-i)+1):
        print("  V", end='')
    print()
