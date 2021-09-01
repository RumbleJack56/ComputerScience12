print("Quadratic Equation Solver  \nMake your equation of the form ax² + bx + c = 0")
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
c=float(input("Enter value of c: "))
D=b**2 - 4*a*c
if D>0:
    r1=(-b + D**(1/2))/(2*a)
    r2=(-b - D**(1/2))/(2*a)
    print("Equation has real and distinct roots. \nThe roots are",r1,"and",r2)
elif D==0:
    r=(-b)/(2*a)
    print("Equation has real and equal roots. \nThe roots are both equal to",r)
elif D<0:
    print("Equation has no real roots.")
