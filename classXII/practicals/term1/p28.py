#7/5/22

import sd

myfile=open('p28.txt','r')
str1=' '
size=0
tsize=0

while str1:
    str1=myfile.readline()
    tsize=tsize+len(str1)
    size=size+len(str1.strip())

print('Total size: ',tsize)
print('Size after removing EOL and blank spaces: ',size)
myfile.close()