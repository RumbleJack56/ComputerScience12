# this is a forever loop
print("Hello Welcome to Geometric Operators")
while True:
    print("Please enter the number corresponding to a shape")


    print("\t1) Square\n\t2) Rectangle\n\t3) Triangle\n\t4) Circle\n\t5) Cube\n\t6) Cuboid\n\t7) Sphere",end="\n\n")

    shape = input()


    if ((shape=='1') or (shape=='2') or (shape=='3')):

        print("What d you want to find? (select the correspinding number)")
        print("\t1) Area\n\t2) Perimeter")



        gfunc = input()

###############################################################################
        #Area of Square
        if((gfunc=='1') and (shape=='1')):

            print("Area of a Square")
            len=int(input("Enter length of Side of Square: "))
            print("Area of square of length",len,"cm is",(len**2))

        #Perimeter of Square
        elif((gfunc=='2') and (shape=='1')):

            print("Perimeter of a Square")
            len=int(input("Enter length of Side of square: "))
            print("Perimeter of Square of length",len,"cm is",(len*4))


###############################################################################
        #Area of Rectangle
        elif((gfunc=='1') and (shape=='2')):

            print("Area of a Rectangle")
            l=int(input("Enter length of Rectangle: "))
            b=int(input("Enter breadth of Rectangle: "))
            print("Area of Rectangle of length",l,"cm and breadth",b,"cm is",(l*b))

        #Perimeter of Rectangle
        elif((gfunc=='2') and (shape=='2')):

            print("Perimeter of a Rectangle")
            l=int(input("Enter length of Rectangle: "))
            b=int(input("Enter breadth of Rectangle: "))
            print("Perimeter of Rectangle of length",l,"cm and breadth",b,"cm is",(2*(l + b)))


###############################################################################
        #Area of Triangle
        elif((gfunc=='1') and (shape=='3')):

            print("Area of a triangle")
            a=int(input("Enter Side 1 of triangle: "))
            b=int(input("Enter Side 2 of triangle: "))
            c=int(input("Enter Side 3 of triangle: "))
            s=(a + b + c)/2
            ar= s*(s-a)*(s-b)*(s-c)
            ar= ar**(1/2)
            print("Area of Triangle of sides",a,"cm,",b,"cm and",c,"cm is",ar)

        #Perimeter of triangle
        elif((gfunc=='2') and (shape=='3')):

            print("Perimeter of a Triangle")
            a=int(input("Enter Side 1 of triangle: "))
            b=int(input("Enter Side 2 of triangle: "))
            c=int(input("Enter Side 3 of triangle: "))
            print("Perimeter of Triangle of sides",a,"cm,",b,"cm and",c,"cm is",(a + b + c))


###############################################################################
    #Circle Specific
    elif ((shape=='4')):
        print("What d you want to find? (select the correspinding number)")
        print("\t1) Area\n\t2) Circumference")

        gfunc = input()

        #Area of Circle
        if((gfunc=='1')):

            print("Area of a Circle")
            r=int(input("Enter Radius of Circle: "))
            print("area of Circle of Radius",r,"cm is",(pi() * r * r))

        #Circumference of Circle
        elif((gfunc=='2')):

            print("Circumference of a Circle")
            r=int(input("Enter Radius of Circle: "))
            print("Circumference of Circle of Radius",r,"cm is",(pi() * r * 2))

###############################################################################

    elif ((shape=='5') and (shape=='6') and (shape=='7')):
        print("What d you want to find? (select the correspinding number)")
        print("\t1) Surface Area\n\t2) Volume")

        gfunc = input()

        #Surface Area of Cube
        if((gfunc=='1') and (shape=='5')):

            print("Surface Area of a Cube")
            len=int(input("Enter length of Side of Cube: "))
            print("Surface area of Cube of length",len,"cm is",(6*(len**2)))

        #Volume of Cube
        elif((gfunc=='2') and (shape=='5')):

            print("Volume of a Cube: ")
            len=int(input("Enter length of Side of Cube: "))
            print("Volume of Cube of length",len,"cm is",(len**3))


###############################################################################
        #Surface Area of Cuboid
        elif((gfunc=='1') and (shape=='6')):

            print("Surface Area of a Cuboid")
            l=int(input("Enter length of Cuboid: "))
            b=int(input("Enter breadth of Cuboid: "))
            b=int(input("Enter height of Cuboid: "))
            print("Surface Area of Cuboid of length",l,"cm, height",h,"cm and breadth",b,"cm is",(2(l*b + b*h + h*l)))

        #Volume of Cuboid
        elif((gfunc=='2') and (shape=='6')):

            print("Volume of a Cuboid")
            l=int(input("Enter length of Cuboid: "))
            b=int(input("Enter breadth of Cuboid: "))
            b=int(input("Enter height of Cuboid: "))
            print("Volume of Cuboid of length",l,"cm, height",h,"cm and breadth",b,"cm is",(l*b*h))


###############################################################################
        #Surface Area of Sphere
        elif((gfunc=='1') and (shape=='7')):

            print("Surface Area of a Sphere")
            r=int(input("Enter Radius of Sphere: "))
            print("Surface area of Sphere of Radius",r,"cm is",(4 * pi() * r * r))

        #Volume of Sphere
        elif((gfunc=='2') and (shape=='7')):

            print("Volume of a Sphere")
            r=int(input("Enter Radius of Sphere: "))
            print("Volume of Sphere of Radius",r,"cm is",(4 / 3 * pi() * r * r * r))

    break
