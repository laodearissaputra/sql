
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql = "SELECT * FROM employee \
       WHERE income > '%d'" % (1000)
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income ))
except:
   print ("Error: unable to fecth data")

db.close()