
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql = "DELETE FROM employee WHERE age > '%d'" % (20)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()