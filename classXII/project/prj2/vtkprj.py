import os
import platform
import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='',database='School')

mycursor=mydb.cursor()

def SIn():
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    name=input("Enter the name: ")
    L.append(name)
    age=int(input("Enter age of student : "))
    L.append(age)
    c=input("Enter the class : ")
    L.append(c)
    city=input("Enter the city of the student : ")
    L.append(city)
    stud=(L)
    sql="insert into student (roll,name,age,class,city) values (%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()

def SV():
    print("Select the search criteria : ")
    print("1. Roll number")
    print("2. Name")
    print("3. Age")
    print("4. City")
    print("5. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
        s=int(input("Enter roll number : "))
        rl=(s,)
        sql="select * from student where roll=%s"
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input("Enter name : ")
        rl=(s,)
        sql="select * from student where name=%s"
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input("Enter age : "))
        rl=(s,)
        sql="select * from student where age=%s"
        mycursor.execute(sql,rl)
    elif ch==4:
        s=input("Enter city : ")
        rl=(s,)
        sql="select * from student where City=%s"
        mycursor.execute(sql,rl)
    elif ch==5:
        sql="select * from student"
        mycursor.execute(sql)   
    res=mycursor.fetchall()
    print("The students details are as follows : ")
    print("(Roll number, Name, Age, Class, City)")
    for x in res:
        print(x)
        
def FEE():
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    feedeposit=int(input("Enter the fee to be deposited : "))
    L.append(feedeposit)
    month=input("Enter month of fee : ")
    L.append(month)
    fee=(L)
    sql="insert into fee (roll,feeDeposit,Month) values (%s,%s,%s)"
    mycursor.execute(sql,fee)
    mydb.commit()

def FEEV():
    print("Please enter the details to view the fee details : ")
    roll=int(input("Enter the roll number of the student whose fee is to be viewed : "))
    sql="Select Student.Roll, Student.Name, Student.Class, sum(fee.feeDeposit), fee.month from Student INNER JOIN fee ON Student.roll=fee.roll and fee.roll = %s"
    rl=(roll,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    for x in res:
        print(x)
    
    
def SR():
    roll=int(input("Enter the roll number of the student to be deleted : "))
    rl=(roll,)
    sql="Delete from fee where roll=%s"
    mycursor.execute(sql,rl)
    sql="Delete from student where roll=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    

def MenuSet(): #Function For The Student Management System
    print("Enter 1 : To add student")
    print("Enter 2 : To view student ")
    print("Enter 3 : To deposit fee ")
    print("Enter 4 : To remove student")
    print("Enter 5 : To view fee of any student")
    
    try: 
        userInput = int(input("Please Select An Above Option: ")) 
    except ValueError:
        exit("\n Please enter an appropriate number.") 
    else:
        print("\n") 
        if(userInput == 1):
            SIn()
        elif (userInput==2):
            SV()
        elif (userInput==3):
            FEE()
        elif (userInput==4):
            SR()
        elif (userInput==5):
            FV()
        else:
            print("Enter an appropriate choice.")       
        
MenuSet()