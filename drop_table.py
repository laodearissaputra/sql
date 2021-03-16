
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

sql = "DROP TABLE employee"

cursor.execute(sql)

print('table drop')

db.close()