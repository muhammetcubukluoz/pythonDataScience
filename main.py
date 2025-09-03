import sqlite3
import os

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):

    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR)
     ''')

    cursor.execute('''
                       CREATE TABLE Courses
                       (
                           id  INTEGER PRIMARY KEY,
                           course_name  VARCHAR NOT NULL,
                           instructor Text,
                           credits INTEGER)
                       ''')

def insert_sample_data(cursor):

    students = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", students)


    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?, ?,?,?)", courses)

    print("Sample Data Insterted Successfully")

def basic_sql_operations(cursor):

    print("------Select All Students------")
    cursor.execute('SELECT * FROM Students')
    records = cursor.fetchall() #List in returns
    for row in records:
        #print(row)
        print(row[0], row[1], row[2], row[3], row[4])

    print("------Select Name, Age Column Students------")
    cursor.execute('SELECT * FROM Students')
    cursor.execute('SELECT name,age FROM Students')
    records = cursor.fetchall()  # List in returns
    print(records)

    print("------Where Age = 20------")
    cursor.execute('SELECT * FROM Students WHERE age = 20')
    records = cursor.fetchall()  # List in returns
    print(records)

    print("------Where With String New York------")
    cursor.execute('SELECT * FROM Students WHERE city = "New York"')
    records = cursor.fetchall()  # List in returns
    for row in records:
        print(row)

    print("------Order By age------")
    cursor.execute('SELECT * FROM Students ORDER BY age')
    records = cursor.fetchall()  # List in returns
    for row in records:
        print(row)

    print("------LIMIT By------")
    cursor.execute('SELECT * FROM Students LIMIT 3')
    records = cursor.fetchall()  # List in returns
    for row in records:
        print(row)

def update_delete_insert_operations(conn,cursor):

    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gamil.com', 'Miami')")
    conn.commit()

    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()

    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()

def aggregate_function(cursor):

    print("------Aggregate Functions Count------")
    cursor.execute('SELECT COUNT(*) FROM Students')
    result = cursor.fetchone() #fetchall
    print(result[0])

    print("------Aggregate Functions Average------")
    cursor.execute('SELECT AVG(age) FROM Students')
    result = cursor.fetchone()  # fetchall
    print(result[0])

    print("------Aggregate Functions MAX - MIN------")
    cursor.execute('SELECT MAX(age), MIN(age) FROM Students')
    result = cursor.fetchone()  # fetchall
    print(result)

    print("------Aggregate Functions GROUP BY------")
    cursor.execute('SELECT COUNT(*),city FROM Students GROUP BY city')
    result = cursor.fetchall()  # fetchall
    print(result)

def query(cursor):

    print("------****------")
    cursor.execute('SELECT * FROM Courses')
    result = cursor.fetchall()
    print(result)

    print("------****------")
    cursor.execute('SELECT course_name, instructor FROM Courses')
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT name,age FROM Students WHERE age = 21')
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT name,city FROM Students WHERE city = "Chicago"')
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT course_name, instructor FROM Courses WHERE instructor = "Dr. Anderson"')
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT name FROM Students WHERE name LIKE  "A%" ')
    result = cursor.fetchone()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT course_name, credits FROM Courses WHERE credits >= 3')
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT * FROM Students ORDER BY name')
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT * FROM Students WHERE age >20 ORDER BY name')
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT * FROM Students WHERE city="New York" or city="Chicago"')
    result = cursor.fetchall()
    for row in result:
        print(row)

    print("------****------")
    cursor.execute('SELECT * FROM Students WHERE city != "New York"')
    result = cursor.fetchall()
    for row in result:
        print(row)


def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        update_delete_insert_operations(conn,cursor)
        aggregate_function(cursor)
        query(cursor)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    main()