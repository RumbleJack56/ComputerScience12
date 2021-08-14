print("Fibonacci Series Calculator")
a1,a2,n=1,1,int(input("Number of terms for Fibonacci Series: "))
an=1
if (n<1):
    print("Invalid Input")
elif (n==1):
    an=1
elif (n==2):
    an=1
else:
    for j in range(3,n+1):
        an = a1 + a2
        a1 = a2
        a2 = an
print(an)
