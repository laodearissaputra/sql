
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql_inner_join = "SELECT  m.member_id, m.name, c.committee_id, c.name FROM members m INNER JOIN committees c ON c.name = m.name"

try:
   cursor.execute(sql_inner_join)
   results = cursor.fetchall()
   for row in results:
        print(row)
except:
   print ("inner join error")

db.close()