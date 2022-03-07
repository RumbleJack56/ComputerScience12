d = {}
a = input("Enter String: ")
for k in a:
    if k not in d:
        d[k]=1
    else:
        d[k]=d[k] + 1
for x in d: print("%2s - %-3s"%(x,d[x]))
