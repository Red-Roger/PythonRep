import sqlite3
from sqlite3 import Error
import os

def select_data(conn, request):

    current_dir = os.getcwd()
    current_script = current_dir + "\\Web 2_6_1\\" + request
    with open(current_script, 'r') as f:
        sql = f.read()

    rows = None
    cur = conn.cursor()
    try:
        cur.execute(sql)
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
        current_script = "query_01.sql"
        projects = select_data(con, current_script)
        print("1. 5 студентів з кращими середніми балами:")
        print ("_________________________________________________")
        print(projects)
        print("\n2. Студенти з кращими балами по кожному предмету: ")
        print ("_________________________________________________")
        current_script = "query_02.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n3. Середній бал у групах по предметах: ")
        print ("_________________________________________________")
        current_script = "query_03.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n4. Середній бал потоку: ")
        print ("_________________________________________________")
        current_script = "query_04.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n5. Курси, які читають викладачі: ")
        print ("_________________________________________________")
        current_script = "query_05.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n6. Список студентів певної групи: ")
        print ("_________________________________________________")
        current_script = "query_06.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n7. Оцінки студентів в окремій групі з певного предмета: ")
        print ("_________________________________________________")
        current_script = "query_07.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n8. Середній бал вчителя по кожному предмету: ")
        print ("_________________________________________________")
        current_script = "query_08.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n9. Список курсів, які відвідує студент: ")
        print ("_________________________________________________")
        current_script = "query_09.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n10. Список курсів, які певному студенту читає певний викладач: ")
        print ("_________________________________________________")
        current_script = "query_10.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n11. Середній бал, який певний викладач ставить певному студентові: ")
        print ("_________________________________________________")
        current_script = "query_11.sql"
        projects = select_data(con, current_script)
        print(projects)
        print("\n12. Оцінки студентів у певній групі з певного предмета на останньому заняті: ")
        print ("_________________________________________________")
        current_script = "query_12.sql"
        projects = select_data(con, current_script)
        print(projects)
