#7/6/22

import sd

myf1=open('p34.txt','r')
myf2=open('p36.txt','a')

s=' '

while s:
    s=myf1.readline()
    myf2.write(s)

myf1.close()
myf2.close()



