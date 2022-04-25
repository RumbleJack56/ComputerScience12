#11/4/22

from random import randint
def fill_list(L , num , min , max):
    for _ in range(num): L.append(randint(min,max))
low , up , elem = int(input("Enter Minimum: ")) , int(input("Enter Maximum: ")) , int(input("Enter total terms: "))
a = []
b = []
fill_list(b,elem,low,up)
print("\n Another set Min:69, Max:420, Total:13")
fill_list(a , min=69 , max=420 , num=13)
print(b)
print(a)

