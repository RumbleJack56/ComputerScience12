a,b = input("Enter String: ") , input("Enter Character: ")[0]
for x in range(len(a)-1,0,-1):
    if b == a[x]:
        print(a[:x]+a[x+1:])
        break
