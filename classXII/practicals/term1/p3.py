#25/3/22

from math import *

#Method 1:
def ar(rad):
    a=pi*rad*rad
    return a
r=float(input("Enter the radius: "))
print("The area is: ",ar(r))

#Method 2:
def ar2(rad):
    return pi*(rad**2)
print(ar2(float(input("Enter Radius: "))))

#Method 3:
ar3 = lambda rad : pi*(r**3)
print(ar3(float(input("Enter Radius: "))))