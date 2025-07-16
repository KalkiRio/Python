import psycopg2

conn=psycopg2.connect(
    host="localhost",
    port="5432",
    password="tiger",
    database="python",
    user="postgres"
)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    subject VARCHAR(100)
)
""")
conn.commit()
# def insert_data():
#     id=int(input("enter id: "))
#     name=input("enter your name: ")
#     subject=input("enter subject: ")
#     cur.execute(f"insert into student values({id},'{name}','{subject}')")
#     conn.commit()

# n=int(input("enter no. of data you want to enter: "))
# for i in range(n):
#     insert_data()

cur.execute("SELECT * from student")
rows = cur.fetchall()
for row in rows:
    print(*row)

cur.close()
conn.close()