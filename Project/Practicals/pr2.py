print("Mathematical Operations")    #Title
#Number Input
n1=float(input("\nEnter first number: "))
n2=float(input("Enter Second number: "))
#operator Input
operator= input("\nEnter Operator ( + , - , * , / , % ): ")
print('') #newline

#Operation based on operator
if(operator=="+"):
    print("The sum of",n1,"and",n2,"is",(n1+n2))
elif(operator=="-"):
    print("The difference of",n1,"and",n2,"is",(n1-n2))
elif(operator=="*"):
    print("The product of",n1,"and",n2,"is",(n1*n2))
elif(operator=="/"):
    print("The quotient of",n1,"and",n2,"is",(n1/n2))
elif(operator=="%"):
    print("The modulo of",n1,"and",n2,"is",(n1%n2))
else: #when input is not a valid operator
    print("Invalid operator!")
