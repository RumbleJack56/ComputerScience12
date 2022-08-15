#15-08-22
#double odd, half even
#random apply
import random

DoHe = lambda L: [2*val if val%2==1 else val//2 for val in L]   #double odd half even

length = random.randrange(7,15)
values = [random.randrange(1,100) for times in range(length)]

print(values)
print(DoHe(values))

