import mysql.connector as mq
import PySimpleGUI as sg
def checkCredentials(h,u,p):
    try:
        conn = mq.connect(host=h,user=u,password=p)
        if conn.is_connected():
            print("Successful Connection")
            return conn
        else:
            print("Connection Failed, wrong details")
            return False
    except:
        print("Connection Failed, wrong details")
        return False

def getdatabases(conn):
    c= conn.cursor()
    c.execute("SHOW DATABASES")
    return [item[0] for item in c]

def loaddb(conn,db):
    c= conn.cursor()
    c.execute("USE "+db)
    c.execute("SHOW TABLES")
    return [item[0] for item in c]
def createdb(conn,db):
    c= conn.cursor()
    c.execute("CREATE DATABASE "+db)
    conn.commit()
def removedb(conn,db):
    c= conn.cursor()
    c.execute("DROP DATABASE "+db)
    conn.commit()
def createtable(conn,table,param):
    c= conn.cursor()
    c.execute("CREATE TABLE "+table+"("+param+")")
    conn.commit()
def removetable(conn,table):
    c= conn.cursor()
    c.execute("DROP TABLE "+table)
    conn.commit()


def tablecols(conn, table):
    c=conn.cursor()
    c.execute("DESC "+table)
    return [item[0] for item in c]

def inserttable(conn,table,data):
    c=conn.cursor()
    try:
        query= "INSERT INTO "+table+" VALUES("+",".join(data)+")"
        c.execute(query)
    except: sg.popup("Data not added",size=(120,90),modal=True,auto_close=True,auto_close_duration=3)

    conn.commit()

def findprimarykey(conn,table):
    c=conn.cursor()
    c.execute("DESC "+table)
    recvdat = [x for x in c]
    print(recvdat)
    for x in range(len(recvdat)):
        if recvdat[x][3]=="PRI":
            return (recvdat[x][0],x)
    else:
        return (recvdat[0][0],0)

def deleteintable(conn,table,data):
    c=conn.cursor()
    pridata=findprimarykey(conn,table)
    print(pridata)
    try: c.execute("Delete from "+table+" where "+pridata[0]+"="+data[pridata[1]])
    except: c.execute("Delete from "+table+" where "+pridata[0]+"=\""+data[pridata[1]]+"\"")
    conn.commit()


def selectfromtable(conn,table):
    c=conn.cursor()
    c.execute("SELECT * FROM "+table)
    return [[str(y) for y in x] for x in c]


def tableformatting(conn,dat,table):
    dat = [tablecols(conn,table)]+dat
    maxl = max([len(line) for line in dat])
    for line in dat:
        print(line)
        while len(line)!=maxl:
            line.append('')
    # print(dat)

    maxlist = []
    for times in range(len(line)):    
        maxval = 0
        for line in dat:
            if len(line[times]) > maxval:
                maxval = len(line[times])
        maxlist.append(maxval)
    strR = "|"
    for length in maxlist:
        strR = strR + r"%-"+str(length)+"s|"
    # print("_"*(sum(maxlist)+len(maxlist)+1))
    out ="‾"*(sum(maxlist)+len(maxlist))+'\n'
    out += str(strR)%tuple(dat[0]) + "\n"
    out += "_"*(sum(maxlist)+len(maxlist)+1)  + "\n"
    for line in dat[1:]:
        # print(line)
        # print(str(strR)%tuple(line))
        out+= str(strR)%tuple(line) + "\n"
    # print("‾"*(sum(maxlist)+len(maxlist)))
    out +="‾"*(sum(maxlist)+len(maxlist))+'\n'
    return out