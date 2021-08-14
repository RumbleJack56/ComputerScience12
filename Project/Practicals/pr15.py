print("Prime Number Checker")
n=int(input("Enter Two digit number: "))
if(9<n and n<100):
    for j in range(2,(n//2)):
        if(n%j==0):
            print("Number is not Prime")
            break
    else:
        print("Number is prime")
else:
    print("Number is not two digit.")
