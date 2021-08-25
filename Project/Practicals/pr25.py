print("String Mutation \n  The program will remove vowels and consonants")
Sen , ts=input("Enter a few Lines: \n") , []
for j in range(0,len(Sen)):
    ts.append(Sen[j])
for num in range(0,len(Sen)):
    a=ts[num].lower
    if(a=="a" or a=="e" or a=="i" or a=="o" or a=="u"):
        ts[num] = ""
    else:
        ts[num] = ts[num].upper()
    print(ts[num], end="")
