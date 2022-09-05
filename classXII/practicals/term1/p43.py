#12/7/22

import sd 

f1 = open("p43a.txt", 'r')
f2 = open("p43b.txt", 'w')

str = " "
while str:
    str = f1.readline().strip('\n')
    w = str.split("~")
    if w[0] == "A":
        f2.write(str+"\n")
        print(str)

f1.close()
f2.close()
