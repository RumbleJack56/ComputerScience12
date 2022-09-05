
#13/7/22

import sd 

f1 = open("p46.txt", 'w')

s=f1.readline()

c=0

for i in s:
    if i.isupper():
        c+=1

print(c)

f1.close(0)
