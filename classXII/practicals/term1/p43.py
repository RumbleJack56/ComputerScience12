#12/7/22

import sd 

f1 = open("p43a.txt", 'r')
f2 = open("p43b.txt", 'w')

str = " "
while str:
    str = f1.readline()
    f2.write(str)

f1.close()
f2.close()
