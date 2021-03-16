
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql_union = "SELECT firstName, lastName FROM employees_sample UNION SELECT contactFirstName, contactLastName FROM customers"

try:
   cursor.execute(sql_union)
   results = cursor.fetchall()
   for row in results:
        print(row)
except:
   print ("Union error")

db.close()