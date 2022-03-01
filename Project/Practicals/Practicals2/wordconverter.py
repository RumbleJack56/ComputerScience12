#write a function to convert number to correspoding in words
#logic 1
ip = input("Enter Number: ")
num = {1:'one' , 2:'two' , 3:'three' , 4:'four' , 5:'five' , 6:'six' , 7:'seven' , 8:'eight' , 9:'nine'}

ip = ip[::-1]
ans = ""
for x in ip:
    ans = num[int(x)] + " " + ans
print(ans)
    



#logic 2
ip = input("Enter Number: ")
num = {1:'one' , 2:'two' , 3:'three' , 4:'four' , 5:'five' , 6:'six' , 7:'seven' , 8:'eight' , 9:'nine'}
tens = {1:'eleven' , 2:'twelve' , 3:'thirty' , 4:'forty' , 5:'fifty' , 6:'sixty' , 7:'seventy' , 8:'eighty' , 9:'ninety'}

ip = ip[::-1]
ans = ""
for x in range(len(ip)):
    if x == 3: ans = 'thousand ' + ans
    if x == 2: ans = "hundred " + ans
    if x in [0,2,3]:
        ans = num[int(ip[x])] + " " + ans
    if x in [1,4]:
        ans = tens[int(ip[x])] + " " + ans

print(ans)
