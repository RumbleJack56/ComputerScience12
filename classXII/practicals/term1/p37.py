#7/6/22

import sd

myfile=open('p37.txt','w+')

myfile.writelines('Hye')
myfile.flush()
input("Next: ")
myfile.writelines('\nThe return of Hi')
myfile.flush()
input("Next: ")
myfile.writelines('\nHi, the wrath of Hello')
myfile.flush()
input("Next: ")
myfile.writelines('\nThe last Hi')
myfile.close()


print('Data saved in the file.')