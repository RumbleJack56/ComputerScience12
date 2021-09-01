print("String Mutation \n  The program will remove vowels and uppercase the consonants")
Sen , ts=input("Enter a few Lines: \n") , []
for j in range(0,len(Sen)):
    ts.append(Sen[j])
for num in range(0,len(Sen)):
    a=ts[num]
    if a in "AEIOUaeiou":
        ts[num] = ""
    else:
        ts[num] = ts[num].upper()
    print(ts[num], end="")
