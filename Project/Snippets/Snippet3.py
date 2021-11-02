n , a = input("Enter String:") , 0
for j in n:
    if j in "1234567890":
        a+=int(j)
print("Result is",a)

n = input("String Here : ")
L = list[n]
b = []
for i in L:
    if L.isdigit():
        b.append(int(L))
sum = 0
for i in b:
    sum+=i
print(sum)
