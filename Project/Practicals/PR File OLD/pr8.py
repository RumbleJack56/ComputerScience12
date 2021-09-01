print("Summation and Factorial Finder")
n = int(input("Enter Natural Number limit for factorial and Summation:"))
factorial,sum=1,0
if n<=0:
    print("Invalid Number, Please enter positive natural number")
else:
    sum=n*(n+1)/2
    for num in range(1,n+1):
        factorial*=num
    print("Sum of numbers till",n,"is",sum)
    print("Product of numbers till",n,"is",factorial)
    
