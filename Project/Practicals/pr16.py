print("Palindrome Check")
n=int(input(("Enter Number: ")))
if(n<0):
    print("Negative numbers are non-palindromic.")
else:
    rev,fr=0,n
    while(fr>0):
        dig=fr%10
        rev= 10*rev + dig
        fr=fr//10
    if(rev==n):
        print("The number",n,"is a palindrome.")
    else:
        print("The number",n,"is not a palindrome.")
