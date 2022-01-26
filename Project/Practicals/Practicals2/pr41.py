print("Student Details")
tup = tuple()
for j in range(int(input("Enter Number of Students: "))):
    print("Details of Student",j+1,":")
    tup += (     (input("Name: "),input("Class: "),input("Roll Number: "),input("Percentage: ")) ,      )
print('_'*32)
for j in tup:
    print("|%-12s|%5s|%5s|%-5s|"%(j[0],j[1],j[2],j[3]))
print('|'+'_'*12+'|'+'_'*5+'|'+'_'*5+'|'+'_'*5+'|')

# 3
# Ram
# XIF
# 32
# 99.9
# Raju
# 12
# 30
# 34.2
# Abhishek
# 5
# 7
# 84.4
