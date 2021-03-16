
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql = "INSERT INTO employee(first_name, \
       last_name, age, sex, income) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('pev', 'sa', 27, 'F', 2000)
try:
   cursor.execute(sql)
   print('data insert success')
   db.commit()
except:
   db.rollback()

db.close()