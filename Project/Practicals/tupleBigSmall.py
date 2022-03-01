tup , c = tuple() , 1
while True:
    try: tup += (float(input("Enter Number "+str(c)+" (Blank when end): ")),)
    except: break ; c=0
    c+=1
if c!=0:
    print("Your input Tuple is",tup)
    print("The mean of the Tuple is",sum(tup)/len(tup))
    print("The sum of the Tuple is",sum(tup))
    print("The biggest element is ",max(tup))
    print("The smallest element is",min(tup))
