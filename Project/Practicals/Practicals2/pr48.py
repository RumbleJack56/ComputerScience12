d = {}
for _ in range(int(input("Enter Length of dictionary: "))):
    k , v = input("Key: ") , input("Value: ")
    d[k] = v
for a,b in d.items():
    print("%7s - %-7s"%(a,b))
