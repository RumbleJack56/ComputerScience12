#

def avg(n1,n2,n3,n4):
    av=(n1+n2+n3+n4)/4
    print(av)

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=int(input("Enter a number: "))
avg(a,b,c,d)

def avg2(n1,n2,n3,n4):
    s=0
    l=4
    for k in n1,n2,n3,n4:
        if k=="":
            k=0
            l-=1
        s+=float(k)
    av=(s)/l
    print(av)

a=input("Enter a number: ")
b=input("Enter a number: ")
c=input("Enter a number: ")
d=input("Enter a number: ")
avg2(a,b,c,d)

