import os
import csv
def newrecord():
    print("Add a New Customer Record")
    print("================")
    f=open('hotel.csv','a',newline='\r\n')
    s=csv.writer(f)
    idno=int(input('Enter idno='))
    name=input('Enter name=')
    roomno=input('Enter roomno=')
    amount=float(input('Enter amount='))
    rec=[idno,name,roomno,amount]
    s.writerow(rec)
    f.close()
    print("Record Saved")
    input("Press any key to continue..")

def updaterecord():
    print("Modify a Customer Record")
    print("================")
    f=open('hotel.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter idno you want to modify')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("idno=",rec[0])
            print("Name=",rec[1])
            print("Room No=",rec[2])
            print("amount=",rec[3])
            choice=input("Do you want to modify this record(y/n)")
            if choice=='y' or choice=='Y':
                idno=int(input('Enter New idno='))
                name=input('Enter new name=')
                roomno=input('Enter roomno=')
                amount=float(input('Enter amount='))
                rec=[idno,name,roomno,amount]
                s1.writerow(rec)
                print("Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
            
    
        
    f.close()   
    f1.close()
    os.remove("hotel.csv")
    os.rename("temp.csv","hotel.csv")
    
    input("Press any key to continue..")

def deleterecord():
    f=open('hotel.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter idno you want to delete')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("idno=",rec[0])
            print("Name=",rec[1])
            print("Room No=",rec[2])
            print("amount=",rec[3])
            choice=input("Do you want to delete this record(y/n)")
            if choice=='y' or choice=='Y':
                pass
                print("Record Deleted")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
            
    f.close()
    f1.close()
    os.remove("hotel.csv")
    os.rename("temp.csv","hotel.csv")
    
    input("Press any key to continue..")

def searchrecord():
    print("searchrecord a Record")
    print("===================")
    f=open('hotel.csv','r',newline='\r\n')  
    r=input('Enter idno you want to searchrecord')
    s=csv.reader(f)
    for rec in s:
        if rec[0]==r:
            print("idno=",rec[0])
            print("Name=",rec[1])
            print("Room No=",rec[2])
            print("amount=",rec[3])
        
    f.close()
    input("Press any key to continue..")
def listrecords():
    print("List of All Records")
    print("===================")
    f=open('hotel.csv','r',newline='\r\n')  
    s=csv.reader(f)
    for rec in s:
        print(rec[0],end="\t\t")
        print(rec[1],end="\t\t")
        print(rec[2],end="\t\t")
        print(rec[3])
        
    
    f.close()
    input("Press any key to continue..")

def mainmenu():
    choice=0
    while choice!=6:
        print("\n")
        print("Main Menu")
        print("==========")
        print("1. Add a new Customer Record")
        print("2. Modify Existing Customer Record")
        print("3. Delete Existing Customer Record")
        print("4. Search a Record")
        print("5. List all Records")
        print("6. Exit")
        choice=int(input('Enter your choice'))
        if choice==1:
            newrecord()
        elif choice==2:
            updaterecord()
        elif choice==3:
            deleterecord()
        elif choice==4:
            searchrecord()
        elif choice==5:
            listrecords()
        elif choice==6:
            print("Good Bye")
            break
mainmenu()