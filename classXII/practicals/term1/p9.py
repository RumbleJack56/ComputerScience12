#18/4/22

from random import randint

def bin (l,el):
    mid=len(l)//2
    low=(0)
    high=len(l)-1
    passes=0
    while l[mid]!=el and low<=high:
        if el>l[mid]:
            low=mid+1
        else:
            high=mid-1
        mid=(high+low)//2
        passes+=1
    if low>high:
        return None
    else:
        return mid,passes

a=[]
for _ in range(12):
    a.append(randint(1,100))
a.sort()
print(a)
v=int(input('Enter to search: '))
op = bin(a,v)
print("found at index:",op[0],"in",op[1])



