#6/6/22

import sd

myfile=open('p32.txt','w')

for i in range(2):
    name=input('Enter a name to store in the file: ')
    myfile.write(name)
    myfile.write('\n')

myfile.close()

print('Data saved in the file.')