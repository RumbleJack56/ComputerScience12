print("Factorials")
Fac , n = 1 , int(input("Enter Positive Number: "))
if(n<0):
    "Invalid Input"
elif (n==0):
    print("Factorial of 0 is 1")
elif(n>0):
    for fact in range(1,n+1):
        Fac*=fact
    print("Factorial of",n,"is",Fac)
