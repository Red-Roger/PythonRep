import sqlite3
from sqlite3 import Error
import os

def select_data(conn, request):

    rows = None
    cur = conn.cursor()
    try:
        cur.execute(request)
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows


if __name__ == '__main__':
    
    current_dir = os.getcwd()
    current_db = current_dir + '\\Web 2_6_1\\courses.db'

    with sqlite3.connect(current_db) as con:
        print("1. 5 студентів з кращими середніми балами:")
        print ("_________________________________________________")
        request = "SELECT student_name, ROUND (AVG(rate), 2) as avg_rate FROM students, marks WHERE marks.student_id = students.id GROUP BY student_name ORDER BY avg_rate DESC LIMIT 5"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("2. Студенти з кращими балами по кожному предмету: ")
        print ("_________________________________________________")
        request = "SELECT lesson, student_name, max(rate) as max_rate FROM students, marks, lessons WHERE marks.student_id = students.id AND lessons.id = marks.lesson_id GROUP BY lesson ORDER BY lesson ASC"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("3. Середній бал у групах по предметах: ")
        print ("_________________________________________________")
        request = "SELECT group_id, lesson, ROUND (AVG(rate), 2) as avg_rate FROM students, marks, lessons WHERE marks.student_id = students.id AND lessons.id = marks.lesson_id group by group_id, lesson ORDER BY lesson ASC"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("4. Середній бал потоку: ")
        print ("_________________________________________________")
        request = "SELECT ROUND (AVG(rate), 2) as avg_rate FROM marks"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("5. Курси, які читають викладачі: ")
        print ("_________________________________________________")
        request = "SELECT tutor_name, lesson FROM tutors, lessons WHERE tutor_id = tutors.id ORDER BY tutor_name"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("6. Список студентів певної групи: ")
        # search_param = input ("Номер групи? ")
        search_param = 2
        print ("_________________________________________________")
        request = f"SELECT group_id, student_name FROM students WHERE group_id = {search_param}"
        projects = select_data(con, request)
        print(projects)