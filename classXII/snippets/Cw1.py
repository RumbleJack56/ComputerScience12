from math import *

#simple
def ar(rad):
    a=pi*rad*rad
    return a
r=float(input("Enter the radius: "))
print("The area is: ",ar(r))

#better
def ar2(rad):
    return pi*(rad**2)
print(ar2(float(input("Enter Radius: "))))

#advanced
ar3 = lambda rad : pi*(r**3)
print(ar3(float(input("Enter Radius: "))))
