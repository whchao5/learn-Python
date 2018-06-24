
import mysql.connector

conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()
cursor.execute('create table user (id int(11) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
conn.commit()
cursor.close()