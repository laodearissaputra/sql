
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql = "UPDATE employee SET age = 28 WHERE sex = 'M'"

try:
   cursor.execute(sql)
   print('data update')
   db.commit()
except:
   db.rollback()

db.close()