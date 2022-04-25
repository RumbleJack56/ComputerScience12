#28/3/22
from math import *

def conNum(x):
    if float(x) == round(float(x)): 
        return round(float(x))
    elif float(x) != round(float(x)): 
        return round(float(x),3)

def simpleCalc():
    print("Welcome to Simple Calculator, + adds , - subtracts , x multiplies , / divides , ^ exponents, exit by typing 'out' in operation")
    cv = conNum(input("Enter number: "))
    while True:
        fun = input("Enter operation: ")

        if (fun == "+"): 
    if (fun == "+"): 
        if (fun == "+"): 
            cv += conNum(input("Enter number: "))
            print(cv)
        if (fun == "-"): 
    if (fun == "-"): 
        if (fun == "-"): 
            cv -= conNum(input("Enter number: "))
            print(cv)
        if (fun.lower() in ("x","*") ): 
            cv *= conNum(input("Enter number: "))
            print(cv)
        if (fun == "/"): 
    if (fun == "/"): 
        if (fun == "/"): 
            cv /= conNum(input("Enter number: "))
            print(cv)
        if (fun == "^"): 
    if (fun == "^"): 
        if (fun == "^"): 
            v = conNum(input("Enter number: "))
            cv=pow(cv,v)
            print(cv)
        if (fun.lower() == "out"):
            break

def VolumeCalc():
    print("Welcome to Volume Calculator, write shape name to find volume ")
    shapeType = input("Enter Shape (Cube, Cuboid, Cone, Cylinder, Sphere, Hemisphere, Frustrum): ")

    if shapeType.lower() == "cube":
        print("The Volume of Cube is",
        conNum(input("Enter Side: "))**3)
    if shapeType.lower() == "cuboid":
        print("The Volume of Cuboid is",
        conNum(input("Enter Length: "))*conNum(input("Enter Breadth: "))*conNum(input("Enter Length")))
    if shapeType.lower() == "cone":
        print("The Volume of Cone is",
        pi*(conNum(input("Enter radius: "))**2)*conNum(input("Enter height: "))/3)
    if shapeType.lower() == "":
        print("The Volume of cylinder is",
        pi*(conNum(input("Enter radius: "))**2)*conNum(input("Enter height: ")))
    if shapeType.lower() == "sphere":
        print("The Volume of Sphere is",
        4*pi/3*conNum(input("Enter radius: "))**3)
    if shapeType.lower() == "hemisphere":
        print("The Volume of Hemisphere is",
        2*pi/3*conNum(input("Enter radius: "))**3)
    if shapeType.lower() == "Frustrum":
        print("The Volume of Frustrum is",
        (conNum(input("Enter radius 1: "))**3 - conNum(input("Enter radius 2: "))**3) * pi / 3 * conNum(input("Enter height: ")) )
    
def SAcalc():
    print("Welcome to Surface Area Calculator, write shape name to find Surface Area ")
    shapeType = input("Enter Shape (Cube, Cuboid, Cone, Cylinder, Sphere, Hemisphere, Frustrum): ")

    if shapeType.lower() == "cube":
        print("The Surface Area of Cube is",
        6*conNum(input("Enter Side: "))**2)
    if shapeType.lower() == "cuboid":
        l=conNum(input("Enter Length: "))
        b=conNum(input("Enter Breadth: "))
        h=conNum(input("Enter Length"))
        print("The Surface Area of Cuboid is",2(l*b + b*h + h*l))
    if shapeType.lower() == "cone":
        r = conNum(input("Enter radius: "))
        h = conNum(input("Enter height: "))
        print("The Surface Area of Cone is",
        pi * r * (r + (r**2 + h**2)**(1/2)   ))
    if shapeType.lower() == "":
        r = conNum(input("Enter radius: "))
        h = conNum(input("Enter height: "))
        print("The Surface Area of cylinder is",
        2*pi*r*(r+h))
    if shapeType.lower() == "sphere":
        print("The Surface Area of Sphere is",
        4*pi*conNum(input("Enter radius: "))**2)
    if shapeType.lower() == "hemisphere":
        print("The Surface Area of Hemisphere is",
        3*pi*conNum(input("Enter radius: "))**2)
    if shapeType.lower() == "Frustrum":
        print("The Surface Area of Frustrum is  ",
        (conNum(input("Enter radius 1: ")) + conNum(input("Enter radius 2: "))) * pi * (conNum(input("Enter height: ")) + 2) )






        








optionType = 0
print("Welcome to General Calculator, It has many options such as volume, area, trigonometry, currency, general.")
print("Select what you want to use")

while True:

    optionType = input("Enter your calculator type:\n   1)Volume\n   2)Surface Area\n   3)Trigonometry\n   4)Currency\n   5)General\n   6)Exit\n\n     ")
    if optionType.lower() == "volume" or optionType.lower() == "1":
        VolumeCalc()
    if optionType.lower() == "surface area" or optionType.lower() == "2":
        pass
    if optionType.lower() == "trigonometry" or optionType.lower() == "3":
        pass
    if optionType.lower() == "currency" or optionType.lower() == "4":
        pass
    if optionType.lower() == "general" or optionType.lower() == "5":
        simpleCalc()
    if optionType.lower() == "exit" or optionType.lower() == "6":
        break