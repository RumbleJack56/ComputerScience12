from math import *          #Used for using precise pi

def Validate(val):          #Validates code for integer and float
    if(float(val)==int(val)):
        val = int(val)

def periRect(l,b):
    l,b=float(l),float(b)   #Float making of Values
    peri = 2 * (l + b)      #formula
    Validate(peri)          #Validation
    return peri             #Returns the Perimeter

def periSquare(s):
    s = float(s)            #Float making of Values
    peri = 4 * s            #formula
    Validate(peri)          #Validation
    return peri             #Returns the Perimeter

def circumCircle(r):
    r = float(r)            #Float making of Values
    circum = pi * r * 2     #formula
    Validate(circum)        #Validation
    return circum           #Returns the Circumference

#intro
print("Hello, we will be finding Perimeter of shapes.")

#Selects the shape
shapeSelect = input("Select your shape (Pick the respective number) \n 1)Rectangle \n 2)Square \n 3)Circle \n  ")

#Shape 1 is rectangle
if (shapeSelect=='1'):
    print("You have chosen Rectangle")
    len=input("Enter Length: ")
    bre=input("Enter Breadth: ")
    print("Perimeter of rectangle of Length",len,"cm and breadth",bre,"cm is",periRect(len,bre),"cm.")

#shape 2 is Square
elif (shapeSelect=='2'):
    print("You have chosen Square")
    side=input("Enter Side: ")
    print("Perimeter of Square of Side",side,"cm is",periSquare(side),"cm.")

#shape 3 is Circle
elif (shapeSelect=='3'):
    print("You have chosen Circle")
    rad=input("Enter Radius: ")
    print("Circumference of Circle of radius",rad,"cm by formula π x",rad,"x",rad, "is",circumCircle(rad),"cm.")

else:
    print("Invalid Input, Please try again")
