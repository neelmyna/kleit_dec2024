import pymysql
import sys

class DbOperations:
    def __init__(self):
        pass

    def connect_db(self):
        try:
            connection = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='Root123', database='nithin_db', charset='utf8')
            print('Database connected successfully')
        except pymysql.err.OperationalError as e:
            print('Database connection failed')
            print(e)
        return connection

    def disconnect_db(self, conn):
        try:
            conn.close()
            print('Database dis-connected successfully')
        except:
            print('Database dis-connection failed')

    def read_flight(self):
        airway_company = input('Enter the Airline name: ')
        source_place = input('Enter source of the flight: ')
        destination = input('Enter destination of the flight: ')
        duration = input('Enter duration of the flight in hours: ')
        fare = input('Enter fare of the flight: ')
        return (airway_company, source_place, destination, duration, fare)

    def insert_row(self):
        query = '''insert into flights(airway_company, source_place, destination, duration, fare) values (%s, %s,  %s, %s, %s);'''
        flight = self.read_flight()
        connection = self.connect_db()
        try:
            cursor = connection.cursor()
            count = cursor.execute(query, flight)
            if count == 1:
                print(f'Flight insertion successful')
            else:
                print(f'Flight insertion failed')
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
        except pymysql.err.OperationalError as e:
            print(e)
        except:
            print('Some error occured while inserting the Record')

    def delete_row(self):
        query = 'delete from flights where id = %s'
        id = int(input('Enter Id of the flight to be deleted: '))
        connection = self.connect_db()
        try:
            cursor = connection.cursor()
            count = cursor.execute(query, id)
            if count == 1:
                print(f'Flight with id {id} is deleted')
            else:
                print(f'Flight with id {id} not found')
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
        except:
            print('Some error occured while deleting the Record')

    def search_row(self):
        query = 'select * from flights where id = %s'
        id = int(input('Enter Id of the flight to be searched: '))
        connection = self.connect_db()
        try:
            cursor = connection.cursor()
            count = cursor.execute(query, id)
            if count == 1:
                row = cursor.fetchone()
                print('Flight details are \n', str(row))
            else:
                print(f'Flight with id {id} not found')
            cursor.close()
            self.disconnect_db(connection)
        except:
            print('Some error occured while searching the Record')

    def update_row(self):
        query = 'update flights set fare = %s where id = %s'
        id = int(input('Enter Id of the flight to be updated: '))
        new_fare = float(input('Enter new fare of the flight: '))
        connection = self.connect_db()
        try:
            cursor = connection.cursor()
            count = cursor.execute(query, (new_fare, id))
            if count == 1:
                print(f'Fare of the Flight with id {id} is updated')
            else:
                print(f'Flight with id {id} not found')
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
        except:
            print('Some error occured while updating the Record')

    def listAll(self):
        query = 'select * from flights'
        connection = self.connect_db()
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
            self.disconnect_db(connection)
        except:
            print('Some error occured while searching the Record')

class Menu:
    def __init__(self):
        print('Welcome to Flight Mini Project')

    def exit_program(self):
        sys.exit('End of program')

    def invalid_choice(self):
        print('Invalid choice entered')

    def run_menu(self, db_obj):
        menu = {
            1 : db_obj.insert_row,
            2 : db_obj.search_row,
            3 : db_obj.update_row,
            4 : db_obj.delete_row,
            5 : db_obj.listAll,
            6 : self.exit_program
        }

        while True:
            print('1:Insert 2:Search 3:Update 4:Delete 5:ListAll 6:Exit')
            choice = int(input('Enter your choice: '))
            menu.get(choice, self.invalid_choice)()

    def start_app(self):
        db_obj = DbOperations()
        self.run_menu(db_obj)

menu = Menu()
menu.start_app()