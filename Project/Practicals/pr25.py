print("String Mutation \n  The program will remove vowels and uppercase the consonants")
Sen , ts=input("Enter a few Lines: \n") , []
for j in range(0,len(Sen)):
    ts.append(Sen[j])
for num in range(0,len(Sen)):
    a=ts[num]
    if(a=="a" or a=="A" or a=="e" or a=="E" or a=="i" or a=="I" or a=="o" or a=="O" or a=="u" or a=="U"):
        ts[num] = ""
    else:
        ts[num] = ts[num].upper()
    print(ts[num], end="")
