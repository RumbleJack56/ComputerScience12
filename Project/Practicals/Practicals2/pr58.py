val , d = input("Enter Words: ").split() , {}
for k in val:
    if k[0] not in d:
        d[k[0]] = k
print(d)
