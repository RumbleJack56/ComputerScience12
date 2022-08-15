#15-08-22
#stack employee pop push
EmployeesL = []
top = len(EmployeesL)
def Push(L):
    global top
    name = input("Enter Employee Name: ") 
    L.append(name)
    top=len(L) - 1

def Pop(L):
    if len(L)==0: print("UnderFlow")
    else:
        print("Employee",L.pop(),"was popped.")
        global top
        top = top - 1



Push(EmployeesL)
print(top)