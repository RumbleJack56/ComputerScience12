#15-08-22
import mysql.connector
db = mysql.connector.connect(host ="localhost", user ="root", password ="")
mq = db.cursor()

mq.execute("SHOW DATABASES")
val = mq.fetchall()
print(val)
if ("vartika",) not in val:
    mq.execute("CREATE DATABASE vartika")


mq.execute("SHOW DATABASES")
print(mq.fetchall())


the quick beown fox jumps over a