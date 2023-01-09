import mysql.connector as mq

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
def removedb(conn,db):
    c= conn.cursor()
    c.execute("DROP DATABASE "+db)
def createtable(conn,table,param):
    c= conn.cursor()
    c.execute("CREATE TABLE "+table+"("+param+")")
def removetable(conn,table):
    c= conn.cursor()
    c.execute("DROP TABLE "+table)


def tablecols(conn, table):
    c=conn.cursor()
    c.execute("DESC "+table)
    return len(["" for item in c])