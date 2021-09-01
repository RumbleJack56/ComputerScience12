print("Odd and Even")
Lower = int(input("Enter Lower limit:"))
Upper = int(input("Enter Upper limit:"))

print("List of Odd numbers: ")
for a in range(Lower+1,Upper):
    if((a%2)==1):
        print(a,"is odd.")
print("\nList of Even Numbers: ")
for b in range(Lower+1,Upper):
    if((b%2)==0):
        print(b,"is even.")
