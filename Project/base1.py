while 1==1:
    print("Hello,\n Welcome to Python Conversion system \n We will convert your number from decimal to hexadecimal and binary")
    x=int(input(' Please input a number \n '))
    hexx = str(hex(x))
    binx = str(bin(x))
    hexx = hexx.replace('0x','')
    binx = binx.replace('0b','')
    print(' Your Number is "',x,'" which is  "',hexx,'"  in Hexadecimal and  "',binx,'"  in Binary.',sep='', end='\n\n')
    break
