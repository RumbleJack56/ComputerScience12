#8/4/22

#Method 1: 
from random import random,randint
n=(random()*900+100)//1
print('The number is: ',n)
s = 0
while n >0:
    s +=n%10
    n//=10
print('The sum of the digits is:',s)

#Method 2:
n2 = randint(100,999)
print("The number is:",n2)
print("The sum of digits is",sum([int(k) for k in str(n2)]))