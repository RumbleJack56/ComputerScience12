a = [1 , 3 , 73 , 23 , 54 , 2102 , 32 , 1]
max = a[0]
for times in a:
    for j in a:
        if j > max:
            max = j
print('Largest number in',a,'is',max)
