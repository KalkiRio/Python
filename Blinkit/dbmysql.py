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
            phone bigint check(phone>0 and length(phone)=10) not null,
            username varchar(20) not null unique,
            address varchar(30) default null,
            passwd varchar(300) not null) auto_increment=1001""")

cur.execute("""create table if not exists b_admin(aid int primary key auto_increment,
            a_name varchar(25) not null,
            email varchar(30) default null unique,
            phone bigint check(phone>0 and length(phone)=10) not null unique,
            b_id varchar(6) check(length(b_id)=6) not null unique,
            b_name varchar(20) not null,
            username varchar(20) not null unique,
            address varchar(30) not null,
            passwd varchar(300) not null) auto_increment=1001""")

cur.execute("""create table if not exists products(pid int primary key auto_increment,
            p_name varchar(25) not null,
            p_category varchar(30) default 'unknown',
            quantity int not null,
            price int not null,
            b_id varchar(6),
            foreign key (b_id) references b_admin(b_id) on delete cascade) auto_increment=1001""")


cur.execute("""create table if not exists cart(order_id int primary key auto_increment,
            pid int,
            uid int,
            p_name varchar(25) not null,
            quantity int not null,
            price int not null,
            b_id varchar(6),
            b_name varchar(20),
            foreign key (pid) references products(pid) on delete cascade,
            foreign key (uid) references users(uid) on delete cascade,
            foreign key (b_id) references b_admin(b_id) on delete cascade) auto_increment=10001""")

