stringA = input("enter String for palindrome check: ")
#Converts num to string and
stringB = str(stringA)[::-1]

if stringA==stringB:
    print("Its a palindrome ;)")
else:
    print("Its not a palindrome :(")
#wait till keypress
input()
