# import mysql.connector
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="newspiders",
    port=3306,
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM emp")
for row in cursor.fetchall():
    print(*row)
cursor.close()
conn.close()

# conn=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="tiger",
#     database="newspiders",
#     port=3306,
# )
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM emp")
# for row in cursor.fetchall():
#     print(row)
# cursor.close()
# conn.close()




