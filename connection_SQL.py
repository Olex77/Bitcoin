import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
connection = create_connection("C:\\Users\\74025\\OneDrive\\Documents\\GitHub\\New3\\archive\\Formula1.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

show = "SELECT name FROM sqlite_master WHERE type='table'"
data = execute_read_query(connection, show)
execute_read_query(connection, show)
#for alldata in data:
    #print(alldata)
print(data)

seasons = "SELECT * from seasons"
data = execute_read_query(connection, seasons)
execute_read_query(connection, seasons)
for alldata in data:
    print(alldata)

results = "SELECT * from constructors where constructorID = '6'"
data = execute_read_query(connection, results)
execute_read_query(connection, results)
#for alldata in data:
#    print(alldata)
print(data)

constructor = "PRAGMA table_info(constructors)"
data = execute_read_query(connection, constructor)
execute_read_query(connection, constructor)
#for alldata in data:
    #print(alldata)
print(data)
