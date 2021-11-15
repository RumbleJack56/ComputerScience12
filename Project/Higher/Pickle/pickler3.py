import mysql.connector as mq
db = 'database'
try:
    db = mq.connect(host='localhost' , user='root' , password='',database='feelings')
except:
    db = mq.connect(host='localhost' , user='root' , password='')
    db.cursor().execute("CREATE DATABASE FEELINGS")
    db = mq.connect(host='localhost' , user='root' , password='',database='feelings')
crs = db.cursor()

try: crs.execute("CREATE TABLE vartika (number INT AUTO_INCREMENT PRIMARY KEY, thoughts VARCHAR(255))")
except: pass
crs.execute('INSERT INTO vartika (thoughts) VALUES("beautiful")')
  
crs.execute("SELECT * FROM vartika")
  
result = crs.fetchall()
  
for row in result:
    print(row)
    print("\n")