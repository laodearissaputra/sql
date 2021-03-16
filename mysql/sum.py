
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql_max = "SELECT SUM(`income`) FROM `employee`;"

try:
   cursor.execute(sql_max)
   results = cursor.fetchall()
   for row in results:
        print(row[0])
except:
   print ("Sum error")

db.close()