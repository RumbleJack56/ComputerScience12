inp , upp , low , alpha , dig = input("Enter String: ") , 0 , 0 , 0 , 0
for j in inp:
    if j.isalpha():
        alpha+=1
    if j.isupper():
        upp+=1
    if j.islower():
        low+=1
    if j.isdigit():
        dig+=1
print("There are",upp,"uppercase characters,",low,"lowercase letters, total of",alpha,"alphabets and",dig,"digits")
