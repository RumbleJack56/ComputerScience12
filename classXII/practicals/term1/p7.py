#8/4/22

from random import random
n=(random()*900+100)//1
print('The number is: ',n)
s = 0
while n >0:
    s +=n%10
    n//=10
print('The sum of the digits is:',s)