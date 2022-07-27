import sd,csv

with open('p50.csv') as c:
    mr=csv.reader(c)
    print('%10s'%'EMPNO','%20s'%'EMPNAME','%10s'%'SALARY',)
    for i in mr:
        print('%10s'%i[0],'%20s'%i[1],'%10s'%i[2],)