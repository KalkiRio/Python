import sqlite3
conn=sqlite3.connect("python.db")
cur=conn.cursor()
cur.execute("""create table if not exists student(
    id number(3) primary key,
    name varchar(20),
    subject varchar(10))
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

# def delete_data():
#     del_data=int(input("enter id of student to delete student data: "))
#     cur.execute(f"delete from student where id = {del_data}")
#     conn.commit()

# delete_data()

def see_data():
    data=cur.execute("select * from student")
    # dataset = list(data)
    # print(dataset)
    for i in data:
        print(*i)

see_data()
