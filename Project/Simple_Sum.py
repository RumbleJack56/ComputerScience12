while True:
    print('Please input two numbers to add.')
    x = int(input('Please enter first number: \n'))
    # x = int(numFilter(x))
    y = int(input('Please enter second number: \n'))
    # y = int(numFilter(y))

    sum = x + y
    print("The sum of ",x," and ",y," is ",sum, sep="", end="\n\n\n",)
