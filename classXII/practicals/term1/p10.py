#19/4/22

from random import uniform
print("Lottery number is between 1-100")
a = round(uniform(0,100),4)
print("Random Lottery number is",a)


print("Lottery is won by ticket containing numbers: ")
a = lambda : uniform(1,100)//0.01 /100
print(a(),",",a(),"and",a())