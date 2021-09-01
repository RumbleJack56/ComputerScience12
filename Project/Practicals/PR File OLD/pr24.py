print("Title Case")
A , state= input("Enter String: "), 0
print(A[0].upper(),end="")
for char in A[1:(len(A)-1)]:
    if state==1:
        char = char.upper()
        state=0
    if char==" ":
        state=1
    print(char,end="")
print(A[len(A)-1])
