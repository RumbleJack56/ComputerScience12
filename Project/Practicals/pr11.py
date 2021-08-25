print("Fibonacci Series Calculator")
a1,a2,n,an=0,1,int(input("Number of terms for Fibonacci Series: ")),1
if (n<1):
    print("Invalid Input")
elif (n==1):
    print("0")
elif (n==2):
    print("0 \n1")
else:
    print("0 \n1")
    for j in range(3,n+1):
        an = a1 + a2
        a1 = a2
        a2 = an
        print(an)
