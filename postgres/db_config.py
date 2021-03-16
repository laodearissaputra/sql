import sys
import psycopg2 as pdb


# CREATE THE DATABASE

def creatdb_postgres():
    con = pdb.connect(database="test-sql", user="postgres",
                  password="Rahasia.2021", host="127.0.0.1", port="5432")
    print("Create database test-sql")

#SET UP THE CONNECTION
try:
    con = pdb.connect(database="test-sql", user="postgres",
                      password="Rahasia.2021", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print(ver)

except Exception as e:
    print("Error Postgres %d", e)
    sys.exit(1)

creatdb_postgres()