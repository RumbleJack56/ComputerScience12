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



        if((gfunc=='1') and (shape=='1')):

            print("Area of a Square")

            len=int(input("Enter length of Side of square: "))

            print("area of square of length",len,"cm is",(len**2))



        if((gfunc=='2') and (shape=='1')):

            print("Perimeter of a Square")

            len=int(input("Enter length of Side of square: "))

            print("Perimeter of square of length",len,"cm is",(len*4))



        if((gfunc=='1') and (shape=='2')):

            print("Area of a Rectangle")

            l=int(input("Enter length of Rectangle: "))
            b=int(input("Enter breadth of Rectangle: "))

            print("Area of Recangle of length",l,"cm and breadth",b,"cm is",(l*b))



        if((gfunc=='2') and (shape=='2')):

            print("Perimeter of a Square")

            len=int(input("Enter length of Side of square: "))

            print("area of square of length",len,"cm is",(len*4))


    elif ((shape=='4')):
        print("What d you want to find? (select the correspinding number)")
        print("\t1) Area\n\t2) Circumference")

    elif ((shape=='5')):
        print("What d you want to find? (select the correspinding number)")
        print("\t1) Surface Area\n\t2) Volume")
    break
