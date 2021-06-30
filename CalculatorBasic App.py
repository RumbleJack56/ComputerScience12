#To iterate the app
while True:
    # Welcome Line
    print("Hello,\n Welcome to Python Adder \n We will add, subtract and multiply any two numbers you give us")

    # Number Entry as vaiables X and Y
    x=int(input(' Please input a number \n '))
    y=int(input(' Please input another number \n '))

    # Print addition result statement
    print(' Your Numbers are "',x,' " and " ',y,' "and the sum is" ',(x+y),'"\n', sep="")

    #Print subtraction result Statement
    print(' Your Numbers are "',x,'" and "',y,'" and the difference is "',(x-y),'"\n', sep="")

    #Print product result statement
    print(' Your Numbers are "',x,'" and "',y,'" and the product is "',(x*y),'" \n', sep="")
