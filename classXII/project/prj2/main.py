from funcDec import *
import PySimpleGUI as sg,os
from time import sleep
icon = os.getcwd() + r"\classXII\project\prj2\download.ico"



def runwindow1():

    sg.theme("Light Blue 3")

    layout1 =[[sg.Text("MySQL Connectivity")],
            [sg.Text("Connection Status:"),sg.Text("\"Not Connected\"",key="connstatus")],
            [sg.Text("Host: "),sg.Input(key="host",font=("Calibri",14))],
            [sg.Text("User: "),sg.Input(key="user",font=("Calibri",14))],
            [sg.Text("Pass: "),sg.Input(key="pass",font=("Calibri",14))],
            [sg.Button("Login"),sg.Exit()],]

    window = sg.Window("SQL Project",layout1,size=(720,480),font=("Eras Bold ITC",20),resizable=True,icon=icon)
    
    
    while True:
        event , values = window.Read()
        print(event,values)
        if event in (sg.WINDOW_CLOSED,"Exit"): break
        if event == "Login":
            global conn
            conn = checkCredentials(values["host"],values["user"],values["pass"])
            
            if conn == False: sg.popup_error("No Connection Established, Wrong Crendentials, Try Again")
            else: 
                window["connstatus"].update("\"Connected\"")
                sleep(1)
                window.close()
                runwindow2()
    window.close()


def runwindow2():

    sg.theme("Light Blue 3")

    dblist=getdatabases(conn)
    db_buttons = [[sg.Button(x,size=(20,1),font=("Calibri",14))] for x in dblist]

    layout2 =[[sg.Text("MySQL Status: Connected"),sg.Button("Refresh"),sg.Text(" "*65),sg.Button("Back")],
            [sg.Text("Create Database: "), sg.Button("New Database"),sg.Text(" "*8),sg.Text("Delete Database: "), sg.Button("Remove")],
            [],
            [sg.Text("Choose from Existing Database")],]+ db_buttons + [[sg.Exit()]]   

    window = sg.Window("SQL Project",layout2,size=(1080,720),font=("Eras Bold ITC",20),resizable=True,icon=icon)


    while True:
        event , values = window.Read()
        print(event,values)
        if event in (sg.WINDOW_CLOSED,"Exit"): break
        if event in dblist:
            window.close()
            runwindow3(event)
        if event == "Refresh":
            window.close()
            runwindow2()
        if event == "New Database":
            runcreatedbwindow()
            window.close()
            runwindow2()
        if event == "Remove":
            runremovedbwindow(dblist)
            window.close()
            runwindow2()
        if event == "Back":
            window.close()
            runwindow1()   
    window.close()


def runwindow3(db):

    dbname=db
    sg.theme("Light Blue 3")

    tablelist = loaddb(conn,db)
    tablebuttons = [[sg.Button(x,size=(20,2),font=("Calibri",14))] for x in tablelist]

    layout3 =[[sg.Text("MySQL Status: Connected"),sg.Button("Refresh"),sg.Text(" "*65),sg.Button("Back")],
            [sg.Text("Table Selections")],
            [sg.Text("Create Table: "), sg.Button("New Table"),sg.Text(" "*8),sg.Text("Delete Table: "), sg.Button("Remove")],
            [sg.Text(" ")],
            [sg.Text("Choose from Existing Table")],
            ] + tablebuttons + [[sg.Text(" ")],[sg.Text("_"*50)],[sg.Exit()]]
    
    window = sg.Window("SQL Project",layout3,size=(1080,720),font=("Eras Bold ITC",20),resizable=True,icon=icon)


    while True:
        event , values = window.Read()
        print(event,values)
        if event in (sg.WINDOW_CLOSED,"Exit"): break
        if event in tablelist:
            window.close()
            runwindow4(event)
        if event == "Refresh":
            window.close()
            runwindow3(dbname)
        if event == "New Table":
            runcreatetablewindow()
            window.close()
            runwindow3()
        if event == "Remove":
            runremovetablewindow(tablelist)
            window.close()
            runwindow3(dbname)
        if event == "Back":
            window.close()
            runwindow2()
    window.close()


def runwindow4(table):
    sg.theme("Light Blue 3")

    layout3 =[[sg.Text("MySQL Status: Connected"),sg.Button("Refresh"),sg.Text(" "*65),sg.Button("Back")],
            [sg.Text("Table: "),sg.Text(table)],
            [sg.Text("Table Entry: "), sg.Button("Enter Here"),sg.Text(" "*8),sg.Text("Delete Entry: "), sg.Button("Delete Here")],
            [sg.Text("Find Entry: "), sg.Button("Find Here"),sg.Text(" "*8),sg.Text("Full List: "), sg.Button("Click Here")],
            [sg.Text(" ")],
            [sg.Text("_"*50)],
            [sg.Exit()]]

    window = sg.Window("SQL Project",layout3,size=(1080,720),font=("Eras Bold ITC",20),resizable=True,icon=icon)
    while True:
        event , values = window.Read()
        print(event,values)
        if event in (sg.WINDOW_CLOSED,"Exit"): break
        if event == "Refresh":
            window.close()
            runwindow4(table)
        if event == "Enter Here":
            entertablewindow()
            
        if event == "Delete Here":
            deletetablewindow(tablelist)
        
        if event == "Find Here":
            findtablewindow()
            
        if event == "Click Here":
            listtablewindow()

        if event == "Back":
            window.close()
            runwindow2()
    window.close()

def runcreatedbwindow():
    sg.theme("Light Blue 3")

    layout1 =[[sg.Text("MySQL Status: Connected")],
            [sg.Text("Create Database: ")],
            [sg.Text("Database Name: "),sg.Input(key="dbname",font=("Calibri",14))],
            [sg.Button("Create"),sg.Exit()],]
    window = sg.Window("SQL Project",layout1,size=(720,480),font=("Eras Bold ITC",20),resizable=True,icon=icon)
    while True:
        event , values = window.Read()
        print(event,values)
        if event in (sg.WINDOW_CLOSED,"Exit"): break
        if event == "Create":
            createdb(conn,values['dbname'])
            window.close()

def runremovedbwindow(dblist):
    sg.theme("Light Blue 3")

    layout1 =[[sg.Text("MySQL Status: Connected")],
            [sg.Text("Remove Database: ")],]+[[sg.Button(x,size=(20,1),font=("Calibri",14))] for x in dblist]+[[sg.Exit()],]
    window = sg.Window("SQL Project",layout1,size=(720,720),font=("Eras Bold ITC",20),resizable=True,icon=icon)
    while True:
        event , values = window.Read()
        print(event,values)
        if event in (sg.WINDOW_CLOSED,"Exit"): break
        if event in dblist:
            removedb(conn,event)
            window.close()

def runcreatetablewindow():

    sg.theme("Light Blue 3")

    layout1 =[[sg.Text("MySQL Status: Connected")],
            [sg.Text("Create Table: ")],
            [sg.Text("Table Name: "),sg.Input(key="tablename",font=("Calibri",14),size=(18,1))],
            [sg.Text("Parameters: "),sg.Input(key="tableparam",font=("Calibri",14),size=(60,4))],
            [sg.Button("Create"),sg.Exit()],]
    window = sg.Window("SQL Project",layout1,size=(720,480),font=("Eras Bold ITC",20),resizable=True,icon=icon)
    while True:
        event , values = window.Read()
        print(event,values)
        if event in (sg.WINDOW_CLOSED,"Exit"): break
        if event == "Create":
            createtable(conn,values['tablename'],values['tableparam'])
            window.close()

def runremovetablewindow(tablelist):
    sg.theme("Light Blue 3")

    layout1 =[[sg.Text("MySQL Status: Connected")],
            [sg.Text("Remove table: ")],]+[[sg.Button(x,size=(20,1),font=("Calibri",14))] for x in tablelist]+[[sg.Exit()],]
    window = sg.Window("SQL Project",layout1,size=(720,720),font=("Eras Bold ITC",20),resizable=True,icon=icon)
    while True:
        event , values = window.Read()
        print(event,values)
        if event in (sg.WINDOW_CLOSED,"Exit"): break
        if event in tablelist:
            removetable(conn,event)
            window.close()

def entertablewindow()


runwindow1()