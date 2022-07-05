import sd

#method 1 to read
myfile1 = open("p29.txt", "r")
for line in myfile1:
    print(line,end="")
print()
myfile1.close()


#method 2 to read
myfile1 = open("p29.txt", "r")
for line in myfile1.readlines():
    print(line.rstrip("\n"))

myfile1.close()


#method 3 to read
myfile1 = open("pr29.txt", "r")
a = [line[:-1] for line in myfile1]
print(a)
myfile1.close()

