num = int(input("enter number for palindrome check: "))
#Converts num to string and
revs = int(str(num)[::-1])

if num==revs:
    print("Its a palindrome ;)")
else:
    print("Its not a palindrome :(")
#wait till keypress
input()
