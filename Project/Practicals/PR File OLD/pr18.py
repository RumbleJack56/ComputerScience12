print("Decimal <-----> Binary\n")
state=int(input("What do you want to do?  \n  Binary to Decimal(1) \n  Decimal to Binary(2) \n\t"))
if(state==1):
    b = input("Enter Binary: ")
    bd = int(b,2)
    print("Binary to Decimal of",b,"is",bd)
elif(state==2):
    d = int(input("Enter Decimal: "))
    n , db = d , ''
    while (n>0):
        dig = n%2
        if(dig==1):
            db="1"+db
        else:
            db="0"+db
        n//=2
    print("Decimal to Binary of",d,"is",db)
