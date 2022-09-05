#7/6/22

import sd

myfile=open("p34.txt",'a')

ans='y'

while ans=='y':
    bn=int(input('Enter book number: '))
    bname=input('Enter book name: ')
    au=input('Enter book author: ')
    price=int(input('Enter book price: '))
    brec=str(bn)+','+bname+','+au+','+str(price)
    myfile.write(brec)
    ans=input('More? ')

myfile.close()
