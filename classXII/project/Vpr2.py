import pickle
import time
import os

def set_data():
    rollno = int(input('Enter roll number: '))
    name = input('Enter name: ')
    english = int(input('Enter Marks in English: '))
    maths = int(input('Enter Marks in Maths: '))
    physics = int(input('Enter Marks in Physics: '))
    chemistry = int(input('Enter Marks in Chemistry: '))
    cs = int(input('Enter Marks in CS: '))
    print()
    
    student = {}
    student['rollno'] = rollno
    student['name'] = name
    student['english'] = english
    student['maths'] = maths
    student['physics'] = physics
    student['chemistry'] = chemistry
    student['cs'] = cs
    return student


def display_data(student):
    print('\nSTUDENT DETAILS..')
    print('Roll Number:', student['rollno'])
    print('Name:', student['name'])
    print('English:', student['english'])
    print('Maths:', student['maths'])
    print('Physics:', student['physics'])
    print('Chemistry:', student['chemistry'])
    print('CS:', student['cs'])

def display_data_tabular(student):
    print(student['rollno'], student['name'], student['english'],
          student['maths'], student['physics'], student['chemistry'],
          student['cs'],sep='\t')

def class_result():
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found..')
        print('Go to admin menu to create record')
        return

    print('\nRollno', ' Name', '\tEnglish', 'Maths','Physics','Chemistry','CS')

    while True:
        try:
            student = pickle.load(infile)

            display_data_tabular(student)
        except EOFError:
            break

    infile.close()

def write_record():
    outfile = open('student.dat', 'ab')
    
    while(True):
        pickle.dump(set_data(), outfile)
        ans = input('Wants to enter more record (y/n)?: ')
        if ans in 'nN':
            break

    outfile.close()


def read_records():
    #open file in binary mode for reading
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found..')
        return

    #read to the end of file.
    while True:
        try:
            #reading the oject from file
            student = pickle.load(infile)

            #display the record
            display_data(student)
        except EOFError:
            break

    #close the file
    infile.close()

def search_record():
    #open file in binary mode for reading
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record..')
        return

    found = False
    rollno = int(input('Enter the rollno you want to search: '))
    #read to the end of file.
    while True:
        try:
            #reading the oject from file
            student = pickle.load(infile)
            if student['rollno'] == rollno:
                #display the record
                display_data(student)
                found = True
                break
        except EOFError:
            break
    if found==False:
        print('Record not found!!')

    #close the file
    infile.close()

def delete_record():
    print('\nDELETE RECORD')

    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found to delete..')
        return

    outfile = open("temp.dat","wb")
    found = False

    rollno = int(input('Enter roll number: '))
    while True:
        try:
            #reading the oject from file
            student = pickle.load(infile)

            #display record if found and set flag
            if student['rollno'] == rollno:
                display_data(student)
                found = True
                break
            else:
                pickle.dump(student,outfile)
        except EOFError:
            break

    if found == False:
        print('Record not Found')
        print()
    else:
        print("record found and deleted")    
    infile.close()
    outfile.close()
    os.remove("student.dat")
    os.rename("temp.dat","student.dat")

def modify_record():
    print('\nMODIFY RECORD')    
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found to modify..')
        return

    found = False
    outfile = open("temp.dat","wb")
    rollno = int(input('Enter roll number: '))
    while True:
        try:
            #reading the oject from file
            student = pickle.load(infile)

            #display record if found and set flag
            if student['rollno'] == rollno:

                print('Name:',student['name'])
                ans=input('Wants to edit(y/n)? ')
                if ans in 'yY':
                    student['name'] = input("Enter the name ")

                print('English marks:',student['english'])
                ans=input('Wants to edit(y/n)? ')
                if ans in 'yY':
                    student['english'] = int(input("Enter new marks: "))

                print('Maths marks:',student['maths'])
                ans=input('Wants to edit(y/n)? ')
                if ans in 'yY':
                    student['maths'] = int(input("Enter new marks: "))

                print('Physics marks:',student['physics'])
                ans=input('Wants to edit(y/n)? ')
                if ans in 'yY':
                    student['physics'] = int(input("Enter new marks: "))

                print('Chemistry marks:',student['chemistry'])
                ans=input('Wants to edit(y/n)? ')
                if ans in 'yY':
                    student['chemistry'] = int(input("Enter new marks: "))

                print('CS marks:',student['cs'])
                ans=input('Wants to edit(y/n)? ')
                if ans in 'yY':
                    student['cs'] = int(input("Enter new marks: "))
                
                pickle.dump(student,outfile)
                found = True
                break
            else:
                pickle.dump(student,outfile)
        except EOFError:
            break
    if found == False:
        print('Record not Found')
    else:
        print('Record updated')
        display_data(student)
        
    infile.close()
    outfile.close()
    os.remove("student.dat")
    os.rename("temp.dat","student.dat")

def intro():
    print("==========================================")
    print("ABC School")
    print("SCHOOL RECORDS")
    print("===========================================")
    print()
    time.sleep(1)

def main_menu():
    print("MAIN MENU")
    print("1. REPORT MENU")
    print("2. ADMIN MENU")
    print("3. EXIT")

def report_menu():
    print("REPORT MENU")
    print("1. CLASS RESULT")
    print("2. STUDENT REPORT CARD")
    print("3. BACK TO MAIN MENU")

def admin_menu():
    print("ADMIN MENU")
    print("1. CREATE STUDENT RECORD")
    print("2. DISPLAY ALL STUDENTS RECORDS")
    print("3. SEARCH STUDENT RECORD ")
    print("4. MODIFY STUDENT RECORD ")
    print("5. DELETE STUDENT RECORD ")
    print("6. BACK TO MAIN MENU")

def main():
    intro()
    while(True):
        main_menu()
        choice = input('Enter choice(1-3): ')
        print()

        if choice == '1':
            report_menu()
            rchoice = input('Enter choice(1-4): ')
            if rchoice == '1':
                class_result()
            elif rchoice == '2':
                search_record()
            elif rchoice == '3':
                pass
            else:
                print('Invalid input !!!')
            print()
        
        elif choice == '2':
            admin_menu()
            echoice = input('Enter choice(1-6): ')
            if echoice == '1':
                write_record()
            elif echoice == '2':
                read_records()
            elif echoice == '3':
                search_record()
            elif echoice == '4':
                modify_record()
            elif echoice == '5':
                delete_record()
            elif echoice == '6':
                pass
            else:
                print('Invalid input !!!')
            print()
            
        elif choice == '3':
            break
        else:
            print('Invalid input!!!')
            print()
                            
#call the main function.
main()
