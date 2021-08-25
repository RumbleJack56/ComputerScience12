print("String Anatomy (Character Types)")
stringA = input("Enter String Here: \n")
lc , uc , dig , spec = 0 , 0 , 0 , 0
for j in range (0 , (len(stringA))):
    chk = str(stringA[j])
    if (chk.islower()):
        lc+=1
    elif (chk.isupper()):
        uc+=1
    elif (chk.isnumeric()):
        dig+=1
    elif (chk.isascii()):
        spec+=1
print("The String has",dig,"numeric characters,",(lc + uc),"alphabets of which",lc,"are lowercase and",uc,"are uppercase, while,",spec,"special characters are present")
