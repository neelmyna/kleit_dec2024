import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='Root123', database='nithin_db', charset='utf8')
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

def read_flight():
    airway_company = input('Enter the Airline name: ')
    source_place = input('Enter source of the flight: ')
    destination = input('Enter destination of the flight: ')
    duration = input('Enter duration of the flight in hours: ')
    fare = input('Enter fare of the flight: ')
    return (airway_company, source_place, destination, duration, fare)

def insert_row():
    query = '''insert into flights(airway_company, source_place, destination, duration, fare) values (%s, %s,  %s, %s, %s);'''
    flight = read_flight()
    connection = connect_db()
    try:
        cursor = connection.cursor()
        count = cursor.execute(query, flight)
        if count == 1:
            print(f'Flight insertion successful')
        else:
            print(f'Flight insertion failed')
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except pymysql.err.OperationalError as e:
        print(e)
    except:
        print('Some error occured while inserting the Record')

def delete_row():
    query = 'delete from flights where id = %s'
    id = int(input('Enter Id of the flight to be deleted: '))
    connection = connect_db()
    try:
        cursor = connection.cursor()
        count = cursor.execute(query, id)
        if count == 1:
            print(f'Flight with id {id} is deleted')
        else:
            print(f'Flight with id {id} not found')
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except:
        print('Some error occured while deleting the Record')

def search_row():
    query = 'select * from flights where id = %s'
    id = int(input('Enter Id of the flight to be searched: '))
    connection = connect_db()
    try:
        cursor = connection.cursor()
        count = cursor.execute(query, id)
        if count == 1:
            row = cursor.fetchone()
            print('Flight details are \n', str(row))
        else:
            print(f'Flight with id {id} not found')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Some error occured while searching the Record')

def update_row():
    query = 'update flights set fare = %s where id = %s'
    id = int(input('Enter Id of the flight to be updated: '))
    new_fare = float(input('Enter new fare of the flight: '))
    connection = connect_db()
    try:
        cursor = connection.cursor()
        count = cursor.execute(query, (new_fare, id))
        if count == 1:
            print(f'Fare of the Flight with id {id} is updated')
        else:
            print(f'Flight with id {id} not found')
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except:
        print('Some error occured while updating the Record')

def listAll():
    query = 'select * from flights'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print('The table has no records')
        else:
            rows = cursor.fetchall()
            # displayRows(rows)
            for row in rows:
                print(str(row))
        cursor.close()
        disconnect_db(connection)
    except:
        print('Some error occured while searching the Record')

insert_row()

query = '''insert into flights('airway_company','source_place', 'destination', 'duration', 'fare') values ('indigo', 'coimbatore',  jaipur', 3.5, 8500));'''