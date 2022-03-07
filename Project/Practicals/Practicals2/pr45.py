t1 , t2 = tuple() , tuple()
for x in range(int(input("How Many Values in Tuple 1: "))):
    t1+=(input("Enter Value "+str(x+1)+": "),)
for y in range(int(input("How Many Values in Tuple 2: "))):
    t2+=(input("Enter Value "+str(y+1)+": "),)
print("Tuples are: ",t1,t2,'',sep="\n")
t1 , t2 = t2 , t1
print("New Tuples are:",t1,t2,sep="\n")
