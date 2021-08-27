# str1="safetylaws"
# l=len(str1)
# str2=""
# for i in range(0,l):
#     if(i%2==0):
#         str2+=str1[i].upper()
#     else:
#         str2+=str1[i].lower()
# print("String after Capitalising is : ",str2)

str1="safetylaws"
print("The String after Capitalising is : ",end="")
for i in range(0,len(str1)):
    if(i%2==0):
        print(str1[i].upper(),end="")
    else:
        print(str1[i].lower(),end='')
