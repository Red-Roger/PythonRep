from datetime import datetime
import faker
from random import randint, choice
import sqlite3
import os

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 50
NUMBER_TUTORS = 6
NUMBER_LESSONS = 8
MARKS = 100


def generate_fake_data(number_groups, number_students, number_tutors, number_lessons) -> tuple():
    fake_groups = []  # тут зберігатимемо групи
    fake_students = []  # тут зберігатимемо студентів
    fake_tutors = []  # тут зберігатимемо вчителів
    fake_lessons = []  # тут зберігатимемо предмети
    marks = []

    fake_data = faker.Faker()

    # набір груп
    for j in range(number_groups):
        fake_groups.append(j+1)

    # студенти
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # вчителі
    for _ in range(number_tutors):
        fake_tutors.append(fake_data.name())

    # назви предметів
    for i in range(number_lessons):
        fake_lessons.append(f"Lesson № {i+1}")

    return fake_groups, fake_students, fake_tutors, fake_lessons, marks


def prepare_data(groups, students, tutors, lessons, marks) -> tuple():
    
    for_groups = []
    # готуємо список кортежів назв груп
    for group in groups:
        for_groups.append((group, ))

    # для таблиці students
    for_students = []

    for student in students:
       for_students.append((student, randint(1, NUMBER_GROUPS)))

    # для таблиці tutors
    for_tutors = []

    for tutor in tutors:
       for_tutors.append((tutor, ))

    # для таблиці lessons
    for_lessons = []

    for lesson in lessons:
        for_lessons.append((lesson, randint(1, NUMBER_TUTORS)))

    # для таблиці marks
   
    for_marks = []

    fake_data = faker.Faker()

    for mark in range(NUMBER_STUDENTS):
        for lesson in range (NUMBER_LESSONS):
            for_marks.append((mark+1, lesson+1, randint(1, MARKS), fake_data.date_between(start_date='-30d', end_date = 'today')))


    return for_groups, for_students, for_tutors, for_lessons, for_marks


def insert_data_to_db(groups, students, tutors, lessons, marks) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними
    
    current_dir = os.getcwd()
    current_db = current_dir + '\\Web 2_6_1\\courses.db'

    with sqlite3.connect(current_db) as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        cur.executemany(sql_to_groups, groups)


        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)

        sql_to_tutors = """INSERT INTO tutors(tutor_name)
                               VALUES (?)"""

        cur.executemany(sql_to_tutors, tutors)

        sql_to_lessons = """INSERT INTO lessons(lesson, tutor_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_lessons, lessons)

        sql_to_marks = """INSERT INTO marks(student_id, lesson_id, rate, date_of)
                               VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_marks, marks)

        con.commit()


if __name__ == "__main__":
    groups, students, tutors, lessons, marks = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TUTORS, NUMBER_LESSONS))
    insert_data_to_db(groups, students, tutors, lessons, marks)