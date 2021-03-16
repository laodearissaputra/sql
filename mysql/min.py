
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql_min = "SELECT MIN(`age`) FROM `employee`;"

try:
   cursor.execute(sql_min)
   results = cursor.fetchall()
   for row in results:
        print(row[0])
except:
   print ("Min error")

db.close()