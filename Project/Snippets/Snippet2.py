lis , newL = eval(input("Enter List: ")) , []
[newL.append(x) for x in lis if x not in newL]
print(newL)