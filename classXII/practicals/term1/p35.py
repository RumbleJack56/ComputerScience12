#06-07-2022

#file copy one from another
import sd

#method1
file1 = open("p35a.txt", 'r')
file2 = open("p35b.txt", 'w')
str = " "
while str:
    str = file1.readline()
    file2.write(str)
file1.close()
file2.close()


#method2
file1 = open("p35a.txt", 'r')
file2 = open("p35b.txt", 'w')
[file2.write(line) for line in file1.readlines()]
file1.close()
file2.close()
