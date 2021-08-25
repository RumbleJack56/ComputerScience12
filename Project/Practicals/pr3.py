subjects, iter , marks= ["English" , "Physics" , "Chemistry" , "Maths" , "Computer Science"] , 0 , [0,0,0,0,0]
for sub in subjects:
    marks[iter]=(int(input(("Marks in "+sub+": "))))
    iter+=1
iter=0
for sub in subjects:
    if(marks[iter]>39):
        print("\nYour Grade in",sub,"is ",end="")
        if (marks[iter]>=85):
            print("A")
        elif (marks[iter]>=75):
            print("B")
        elif (marks[iter]>=65):
            print("C")
        elif (marks[iter]>=50):
            print("D")
        elif (marks[iter]>=40):
            print("E")
    else:
        print("\nYour are fail in",sub)
    iter+=1
