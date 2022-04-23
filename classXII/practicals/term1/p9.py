#21/4/22

from random import randint

def bin (l,el):
    mid=len(l)//2
    low=(0)
    high=len(l)-1
    while l[mid]!=el and low<=high:
        if el>l[mid]:
            low=mid+1
        else:
            high=mid-1
        mid=(high+low)//2
    if low>high:
        return None
    else:
        return mid

a=[]
for _ in range(10):
    a.append(randint(1,20))
a.sort()
print(a)
v=int(input('Enter to search: '))
print("found: ",bin(a,v))



