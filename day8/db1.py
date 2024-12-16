# Connecting to the database

import pymysql

def connect_db1():
    connection = pymysql.Connect(host='localhost', port=3306, user='root', password='Root123', database='nithin_db', charset='utf8')
    print('Database connected successfully')
    connection.close()
    print('Database dis-connected successfully')

def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', port=3306, user='root', password='Root123', database='nithin_db', charset='utf8')
        print('Database connected successfully')
        connection.close()
        print('Database dis-connected successfully')
    except pymysql.err.OperationalError as e:
        print('Database connection failed')
        print(e)

connect_db()
