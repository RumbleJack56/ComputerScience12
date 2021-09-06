print("String Based Functions")
s = input("Enter a string: ")
while True:
    c = input("What function do you want to use with the string? (Press Corresponding Number)" + "\n" + "(1)isdigit()" + "\n" + "(2)len()" + "\n" + "(3)isalpha()"+"\n")
    if(c=='1'):
        print("The result of isdigit() function on string '",s,"' is: ",s.isdigit(),sep="")
        break
    elif(c=='2'):
        print("The result of len() function on string '",s,"' is: ",s.isdigit(),sep="")
        break
    elif(c=='3'):
        print("The result of isalpha() function on string '",s,"' is: ",s.isdigit(),sep="")
        break
    else:
        print("Invalid Input, Try again")

# is digit
# len
# isalpha
#Menu driven (if else)
