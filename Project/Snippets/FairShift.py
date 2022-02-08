
# reverse
# 3 codes total


#code 1
list = [1,2,5,7,3,-1]
newL = []
for x in list: newL.insert(0,x)
print(newL)

#code 2
list = [1,2,5,7,3,-1]
newL = list[::-1]
print(newL)

#code 3
lis3 = [1,2,5,7,3,-1]
c=-1
for x in lis3:
    c+=1
for x in range(c):
    lis3[x] , lis3[c-x]  = lis3[c-x] , lis3[x]
print(lis3)


#reverse item backwards
lis = [12,1,43,234,95,38,85,5]
nLis = [int(str(x)[::-1]) for x in lis if len(str(x))>1]
print(nLis)




#sQUARES ELEMENT IN LIST
print("Output is:\n"+str([x**2 for x in eval(input("Enter List with Formatting:\n")) if int(x)==x]))

#duplicate list items remove
lis , val = eval(input("Enter List: ")) , eval(input("Enter Item to remove: "))
newL = [x for x in lis if x!=val]
print(newL)
