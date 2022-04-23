#28/3/22

from math import *

def conNum(x):
    if float(x) == round(float(x)): 
        return round(float(x))
    elif float(x) != round(x): 
        return float(x)





print("Welcome to Simple Calculator, + adds , - subtracts , x multiplies , / divides , ^ exponents")
cv = conNum(input("Enter number: "))
while True:
    fun = input("Enter operation: ")

    if (fun == "+"): 
        cv += conNum(input("Enter number: "))
        print(cv)
    
    if (fun == "-"): 
        cv -= conNum(input("Enter number: "))
        print(cv)

    if (fun.lower() == "x"): 
        cv *= conNum(input("Enter number: "))
        print(cv)

    if (fun == "/"): 
        cv /= conNum(input("Enter number: "))
        print(cv)

    if (fun == "^"): 
        v = conNum(input("Enter number: "))
        cv=pow(cv,v)
        print(cv)
        