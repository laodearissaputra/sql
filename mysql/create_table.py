
import mysql.connector

db = mysql.connector.connect(host='localhost',database='sql-test',user='bithealth',password='Rahasia.2021')

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS employee")

sql = """CREATE TABLE employee (
         first_name  CHAR(20) NOT NULL,
         last_name  CHAR(20),
         age INT,  
         sex CHAR(1),
         income FLOAT )"""

cursor.execute(sql)

print('table create')

db.close()