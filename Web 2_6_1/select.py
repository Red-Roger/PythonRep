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
        request = "SELECT student_name, ROUND (AVG(rate), 2) as avg_rate \
                   FROM students, marks \
                   WHERE marks.student_id = students.id \
                   GROUP BY student_name \
                   ORDER BY avg_rate DESC \
                   LIMIT 5"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("2. Студенти з кращими балами по кожному предмету: ")
        print ("_________________________________________________")
        request = "SELECT lesson, student_name, max(rate) as max_rate \
                   FROM students, marks, lessons \
                   WHERE marks.student_id = students.id AND lessons.id = marks.lesson_id \
                   GROUP BY lesson \
                   ORDER BY lesson ASC"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("3. Середній бал у групах по предметах: ")
        print ("_________________________________________________")
        request = "SELECT group_id, lesson, ROUND (AVG(rate), 2) as avg_rate \
                   FROM students, marks, lessons \
                   WHERE marks.student_id = students.id AND lessons.id = marks.lesson_id \
                   GROUP BY group_id, lesson \
                   ORDER BY lesson ASC"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("4. Середній бал потоку: ")
        print ("_________________________________________________")
        request = "SELECT ROUND (AVG(rate), 2) as avg_rate \
                   FROM marks"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("5. Курси, які читають викладачі: ")
        print ("_________________________________________________")
        request = "SELECT tutor_name, lesson \
                   FROM tutors, lessons \
                   WHERE tutor_id = tutors.id \
                   ORDER BY tutor_name"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("6. Список студентів певної групи: ")
        # search_param = input ("Номер групи? ")
        search_param = 2
        print ("_________________________________________________")
        request = f"SELECT group_id, student_name \
                    FROM students \
                    WHERE group_id = {search_param}"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("7. Оцінки студентів в окремій групі з певного предмета: ")
        # search_param = input ("Номер групи? ")
        # search_param2 = input ("ID предмета? ")
        search_param = 2
        search_param2 = 3
        print ("_________________________________________________")
        request = f"SELECT group_id, lesson, student_name, rate \
                    FROM students, lessons, marks \
                    WHERE marks.student_id = students.id AND lessons.id = marks.lesson_id \
                    AND group_id = {search_param} AND lessons.id = {search_param2} \
                    ORDER BY group_id, lesson"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("8. Середній бал вчителя по кожному предмету: ")
        print ("_________________________________________________")
        request = "SELECT lesson, tutor_name, ROUND (AVG (rate), 2) \
                   FROM marks, lessons, tutors \
                   WHERE tutors.id = lessons.tutor_id AND lessons.id = marks.lesson_id \
                   GROUP BY tutor_name, lesson_id \
                   ORDER BY lesson"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("9. Список курсів, які відвідує студент: ")
        # search_param = input ("Номер студента? ")
        search_param = 46
        print ("_________________________________________________")
        request = f"SELECT student_name, lesson \
                    FROM students, lessons, marks \
                    WHERE students.id = marks.student_id AND lessons.id = marks.lesson_id \
                    AND  students.id = {search_param}"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("10. Список курсів, які певному студенту читає певний викладач: ")
        # search_param = input ("ID викладача? ")
        # search_param2 = input ("ID студента? ")
        search_param = 1
        search_param2 = 37
        print ("_________________________________________________")
        request = f"SELECT tutor_name, student_name, lesson \
                    FROM marks, lessons, tutors, students \
                    WHERE tutors.id = lessons.tutor_id AND lessons.id = marks.lesson_id AND marks.student_id = students.id \
                    AND tutor_id = {search_param} AND student_id = {search_param2}"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("11. Середній бал, який певний викладач ставить певному студентові: ")
        # search_param = input ("ID викладача? ")
        # search_param2 = input ("ID студента? ")
        search_param = 1
        search_param2 = 37
        print ("_________________________________________________")
        request = f"SELECT tutor_name, student_name, ROUND (AVG (rate), 2) \
                    FROM marks, lessons, tutors, students \
                    WHERE tutors.id = lessons.tutor_id AND lessons.id = marks.lesson_id AND marks.student_id = students.id \
                    AND tutor_id = {search_param} AND student_id = {search_param2} \
                    GROUP BY tutor_name, student_name"
        projects = select_data(con, request)
        print(projects)
        print ("")
        print("12. Оцінки студентів у певній групі з певного предмета на останньому занятт: ")
        # search_param = input ("Номер групи? ")
        # search_param2 = input ("ID предмета? ")
        search_param = 1
        search_param2 = 2
        print ("_________________________________________________")
        request = f"SELECT students.group_id, lessons.lesson, students.student_name, rate, MAX (marks.date_of) \
                    FROM marks, lessons, students \
                    WHERE lessons.id = marks.lesson_id AND marks.student_id = students.id \
                    AND students.group_id = {search_param} AND lessons.ID = {search_param2} \
                    GROUP BY students.group_id, lessons.lesson, students.student_name, rate"
        projects = select_data(con, request)
        print(projects)