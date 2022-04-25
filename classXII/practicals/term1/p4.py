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
            cv += conNum(input("Enter number: "))
            print(cv)
        if (fun == "-"): 
            cv -= conNum(input("Enter number: "))
            print(cv)
        if (fun.lower() in ("x","*") ): 
            cv *= conNum(input("Enter number: "))
            print(cv)
        if (fun == "/"): 
            cv /= conNum(input("Enter number: "))
            print(cv)
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
        conNum(input("Enter Length: "))*conNum(input("Enter Breadth: "))*conNum(input("Enter Height: ")))
    if shapeType.lower() == "cone":
        print("The Volume of Cone is",
        pi*(conNum(input("Enter radius: "))**2)*conNum(input("Enter height: "))/3)
    if shapeType.lower() == "cylinder":
        print("The Volume of cylinder is",
        pi*(conNum(input("Enter radius: "))**2)*conNum(input("Enter height: ")))
    if shapeType.lower() == "sphere":
        print("The Volume of Sphere is",
        4*pi/3*conNum(input("Enter radius: "))**3)
    if shapeType.lower() == "hemisphere":
        print("The Volume of Hemisphere is",
        2*pi/3*conNum(input("Enter radius: "))**3)
    if shapeType.lower() == "frustrum":
        print("The Volume of Frustrum is",fabs(
        (conNum(input("Enter radius 1: "))**3 - conNum(input("Enter radius 2: "))**3) * pi / 3 * conNum(input("Enter height: ")) ))
    
def SAcalc():
    print("Welcome to Surface Area Calculator, write shape name to find Surface Area ")
    shapeType = input("Enter Shape (Cube, Cuboid, Cone, Cylinder, Sphere, Hemisphere, Frustrum): ")

    if shapeType.lower() == "cube":
        print("The Surface Area of Cube is",
        6*conNum(input("Enter Side: "))**2)
    if shapeType.lower() == "cuboid":
        l=conNum(input("Enter Length: "))
        b=conNum(input("Enter Breadth: "))
        h=conNum(input("Enter Height: "))
        print("The Surface Area of Cuboid is",2*(l*b + b*h + h*l))
    if shapeType.lower() == "cone":
        r = conNum(input("Enter radius: "))
        h = conNum(input("Enter height: "))
        print("The Surface Area of Cone is",
        pi * r * (r + (r**2 + h**2)**(1/2)   ))
    if shapeType.lower() == "cylinder":
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

def TrigCalc():
    a = lambda x,y: x+" of "+str(y)+" is "+str(eval(x+"("+str(y)+")"))
    print("Welcome to trignometric calculator, What operation would you like to perform?")
    trigOp = input("Enter function(sin,cos,tan,asin,acos,atan): ").lower()
    if trigOp == "sin": print(a(trigOp , float(input("Enter Value: "))))
    elif trigOp == "cos": print(a(trigOp , float(input("Enter Value: "))))
    elif trigOp == "tan": print(a(trigOp , float(input("Enter Value: "))))
    elif trigOp == "asin": print(a(trigOp , float(input("Enter Value: "))))
    elif trigOp == "acos": print(a(trigOp , float(input("Enter Value: "))))
    elif trigOp == "atan": print(a(trigOp , float(input("Enter Value: "))))

def CashCalc():
    print("Welcome to Currency convertor: it converts the currencies to different forms")
    base = input("Enter a supported currency(USD,EUR,JPY,GBP,AUD,CAD,INR): ").upper()
    val = float(input("Enter amount:"))
    convertto = input("Enter 2nd supported currency(USD,EUR,JPY,GBP,AUD,CAD,INR): ").upper()
    if base=="USD":
        if convertto=="USD":print("Exchange Value is",val*1)
        if convertto=="EUR":print("Exchange Value is",val*0.93)
        if convertto=="JPY":print("Exchange Value is",val*127.71)
        if convertto=="GBP":print("Exchange Value is",val*0.78)
        if convertto=="AUD":print("Exchange Value is",val*1.4)
        if convertto=="CAD":print("Exchange Value is",val*1.27)
        if convertto=="INR":print("Exchange Value is",val*76.69)
    if base=="EUR":
        if convertto=="USD":print("Exchange Value is",val*1.07)
        if convertto=="EUR":print("Exchange Value is",val*1)
        if convertto=="JPY":print("Exchange Value is",val*136.97)
        if convertto=="GBP":print("Exchange Value is",val*0.84)
        if convertto=="AUD":print("Exchange Value is",val*1.5)
        if convertto=="CAD":print("Exchange Value is",val*1.37)
        if convertto=="INR":print("Exchange Value is",val*82.17)
    if base=="JPY":
        if convertto=="USD":print("Exchange Value is",val*0.0078)
        if convertto=="EUR":print("Exchange Value is",val*0.0073)
        if convertto=="JPY":print("Exchange Value is",val*1)
        if convertto=="GBP":print("Exchange Value is",val*0.0062)
        if convertto=="AUD":print("Exchange Value is",val*0.011)
        if convertto=="CAD":print("Exchange Value is",val*0.010)
        if convertto=="INR":print("Exchange Value is",val*0.60)
    if base=="GBP":
        if convertto=="USD":print("Exchange Value is",val*1.27)
        if convertto=="EUR":print("Exchange Value is",val*1.19)
        if convertto=="JPY":print("Exchange Value is",val*162.54)
        if convertto=="GBP":print("Exchange Value is",val*1)
        if convertto=="AUD":print("Exchange Value is",val*1.78)
        if convertto=="CAD":print("Exchange Value is",val*1.62)
        if convertto=="INR":print("Exchange Value is",val*97.62)
    if base=="AUD":
        if convertto=="USD":print("Exchange Value is",val*0.71)
        if convertto=="EUR":print("Exchange Value is",val*0.67)
        if convertto=="JPY":print("Exchange Value is",val*91.2)
        if convertto=="GBP":print("Exchange Value is",val*0.56)
        if convertto=="AUD":print("Exchange Value is",val*1)
        if convertto=="CAD":print("Exchange Value is",val*0.91)
        if convertto=="INR":print("Exchange Value is",val*54.77)

    if base=="CAD":
        if convertto=="USD":print("Exchange Value is",val*0.78)
        if convertto=="EUR":print("Exchange Value is",val*0.73)
        if convertto=="JPY":print("Exchange Value is",val*100.04)
        if convertto=="GBP":print("Exchange Value is",val*0.62)
        if convertto=="AUD":print("Exchange Value is",val*1.10)
        if convertto=="CAD":print("Exchange Value is",val*1)
        if convertto=="INR":print("Exchange Value is",val*60.08)
    if base=="INR":
        if convertto=="USD":print("Exchange Value is",val*0.013)
        if convertto=="EUR":print("Exchange Value is",val*0.012)
        if convertto=="JPY":print("Exchange Value is",val*1.67)
        if convertto=="GBP":print("Exchange Value is",val*0.010)
        if convertto=="AUD":print("Exchange Value is",val*0.018)
        if convertto=="CAD":print("Exchange Value is",val*0.017)
        if convertto=="INR":print("Exchange Value is",val*1)



optionType = 0
print("Welcome to General Calculator, It has many options such as volume, area, trigonometry, currency, general.")
print("Select what you want to use")

while True:

    optionType = input("Enter your calculator type:\n   1)Volume\n   2)Surface Area\n   3)Trigonometry\n   4)Currency\n   5)General\n   6)Exit\n\n     ")
    if optionType.lower() == "volume" or optionType.lower() == "1":
        VolumeCalc()
    if optionType.lower() == "surface area" or optionType.lower() == "2":
        SAcalc()
    if optionType.lower() == "trigonometry" or optionType.lower() == "3":
        TrigCalc()
    if optionType.lower() == "currency" or optionType.lower() == "4":
        CashCalc()
    if optionType.lower() == "general" or optionType.lower() == "5":
        simpleCalc()
    if optionType.lower() == "exit" or optionType.lower() == "6":
        break