#27/7/22

import sd,csv

with open('p50.csv') as c:
    mr=csv.reader(c)
    co=0
    s=0
    
    print('%10s'%'EMP. NO.','%20s'%'EMP. NAME','%10s'%'SALARY',)
    for i in mr:
        print('%10s'%i[0],'%20s'%i[1],'%10s'%i[2])
        s+=int(i[2])
        if int(i[2])>8000:
            co+=1

    print("Sum of salaries- ",s)
    print('Number of employees with salary more than 7000- ',co)
