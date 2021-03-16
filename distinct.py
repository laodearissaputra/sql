
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql_distinct = "SELECT DISTINCT `age` FROM `employee`;"
try:
   cursor.execute(sql_distinct)
   results = cursor.fetchall()
   for row in results:
        print(row[0])
except:
   print ("Aggregate error")

db.close()