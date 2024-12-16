import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', port=3306, user='root', password='Root123', database='nithin_db', charset='utf8')
        print('Database connected successfully')
    except pymysql.err.OperationalError as e:
        print('Database connection failed')
        print(e)
    return connection

def disconnect_db(conn):
    try:
        conn.close()
        print('Database dis-connected successfully')
    except:
        print('Database dis-connection failed')

connection = connect_db()
disconnect_db(connection)