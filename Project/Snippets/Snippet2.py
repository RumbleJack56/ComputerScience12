# def calculate_area(b=1, h=1, shapeType=''):
#     if (shapeType.lower() =='triangle'):
#         ar = b * h / 2
#         return ar
#     elif (shapeType.lower() == 'rectangle'):
#         ar = b * h
#         return ar
#     else:
#         print("invalid input")
#
# base = int(input("Base: "))
# height = int(input("Height: "))
# Shape = input("Tell Shape (Rectangle or Triangle): ")
#
# areaR = calculate_area(base, height, Shape)
#
# print(areaR)
##########################################################################

def convertDollar(amount_in_dollar , dollar_to_rupee):
    amount_in_rupee = amount_in_dollar * dollar_to_rupee
    return amount_in_rupee

x = convertDollar(int(input("Enter Amount in Dollars: ")),int(input("Enter Dollar to rupee convertion rate: ")))
print("Value in rupee is",x)    
