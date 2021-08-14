def rect(l,b):
    ar=l * b
    return ar
def tri(s1,s2,s3):
    s= (s1+s2+s3)/2
    ar= ( s * (s-s1) * (s-s2) * (s - s3) )**(1/2)
    return ar
def circ(r):
    ar=3.1415 * r * r
    return ar

print("Area of Shapes")
shape = int(input("Select your shape: \n\tRectangle (1)  \n\tTriangle (2)  \n\tCircle (3)\n\t"))
if (shape==1):
    x = rect(float(input("Enter Length: ")),float(input("Enter Breadth: ")))
    print("The area of rectangle is",x)
elif (shape==2):
    x = tri(float(input("Enter Side 1: ")),float(input("Enter Side 2: ")),float(input("Enter Side 3: ")))
    print("The Area of Triangle is",x)
elif (shape==3):
    x = circ(float(input("Enter Radius: ")))
    print("The area of circle is",x)
else:
    print("Invalid input")
