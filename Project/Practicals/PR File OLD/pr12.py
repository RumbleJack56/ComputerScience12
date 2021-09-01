print("Multipliation Tables")
n=int(input("Enter Number: "))
print("Table of",n,"is:")
for j in range(1,11):
    nj = n * j
    print(n,"x",str(j).zfill(2),"=",nj)
