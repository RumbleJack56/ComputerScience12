print("String Palindrome Check")
stringA = input("Enter String for palindrome check: ")
stringB = str(stringA)[::-1]
if stringA==stringB:
    print("Its a palindrome ;)")
else:
    print("Its not a palindrome :(")
