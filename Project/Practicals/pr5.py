print("The Greatest Number")
n1=float(input("Enter First Number: "))
n2=float(input("Enter Second Number: "))
n3=float(input("Enter Third Number: "))
if (n1>n2 and n1>n3):
    print(n1,"is greatest number among the three")
elif (n2>n1 and n2>n3):
    print(n2,"is greatest number among the three")
elif (n3>n2 and n3>n1):
    print(n3,"is greatest number among the three")
elif (n1>n2 and n1==n3):
    print("The first and second (",n1,") are equal and greatest among the three")
elif (n1>n3 and n1==n2):
    print("The first and third (",n1,") are equal and greatest among the three")
elif (n2>n1 and n2==n3):
    print("The second and third (",n2,") are equal and greatest among the three")
elif (n1==n2 and n2==n3):
    print("All three are equal")
else:
    print("Invalid Input")
