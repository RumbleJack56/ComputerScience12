n_inp = input()
a , q , x= input().split() , [] , input().split()
x , y = int(x[0]) , int(x[1])
for j in range(len(a)):
    for k in range(j+1,len(a)+1):
        q.extend([a[j:k]])
count = len([x for m in q if m.count('0')>x and m.count('1')>y])
print(count)