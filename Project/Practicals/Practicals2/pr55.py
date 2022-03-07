d = {'a':1, 'b':2, 'c':3}
print(d)
for t in range(int(input("Enter the number of key-value pairs: "))):
    k , v = input("Enter Key: ") , input("Enter Value: ")
    d.update({k:v})
    print(d)
