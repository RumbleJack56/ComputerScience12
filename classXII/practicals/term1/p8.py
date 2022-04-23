#21/4/22

from random import randint
def fill_list(L , num , min , max):
    for _ in range(num): L.append(randint(min,max))
low , up , elem = int(input("Enter Minimum: ")) , int(input("Enter Maximum: ")) , int(input("Enter total terms: "))
a = []
b = []
fill_list(b,elem,low,up)
fill_list(a , min=420 , max=4200 , num=69)
print(b)
print(a)