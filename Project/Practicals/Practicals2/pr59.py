name=[]
department=[]
salary=[]
details={'Employee Name:':name,'Department:':department,'Salary:':salary}

for i in range(int(input('Total Number of records: '))):
    name.append(input("Enter employee name: "))
    department.append(input('Enter employee department: '))
    salary.append(input('Enter employee salary: '))

for key,val in details.items():
    print("%15s : %-15s"%(key,val))
