def DoubleIt(mylist1):
    for k in range(len(mylist1)):
        mylist1[k]= mylist1[k]*2
mylist = [10,20,30,40,50,60]
DoubleIt(mylist)
print("Output: ",mylist)