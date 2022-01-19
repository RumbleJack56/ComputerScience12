n = input().split()
m , n = int(n[1]) , int(n[0])
lis = input().split()
lis = [int(x) for x in lis]
num_com = input()
out = []
for _ in range(int(num_com)):
    a = input().split()
    a = [int(x) for x in a]
    if a[0]==1:
        lis[a[1]] = a[2]
    if a[0]==2:
        count = 0
        for x in lis:
            if x % m == a[1]:
                count+=1
        out.append(count)
for j in out:
    print(j)