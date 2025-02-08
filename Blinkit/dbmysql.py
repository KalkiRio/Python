import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="blinkit",
    port=3306,
)
cur=conn.cursor()

cur.execute("""create table if not exists users(uid int primary key auto_increment,
            c_name varchar(25) not null,
            email varchar(30) default null,
            phone decimal(10) check(phone>0 and length(phone)=10) not null,
            username varchar(20) not null unique,
            address varchar(30) default null,
            passwd varchar(300) not null) auto_increment=1001""")

