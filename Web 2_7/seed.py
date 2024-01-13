from connect_db import session
from models import Groups, Students, Tutors, Lessons, Marks

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


if __name__ == "__main__":
    groups, students, tutors, lessons, marks = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_TUTORS, NUMBER_LESSONS))

    for group in groups:
        groups2add = Groups(group_name=group[0])
        session.add(groups2add)

    for student in students:
        student2add = Students(student_name = student[0], group_id = student[1] )
        session.add(student2add)
    
    for tutor in tutors:
        tutor2add = Tutors(tutor_name=tutor[0])
        session.add(tutor2add)

    for les in lessons:
        lesson2add = Lessons(lesson = les[0], tutor_id = les[1] )
        session.add(lesson2add)

    for mark in marks:
        mark2add = Marks(student_id = mark[0], lesson_id = mark[1], rate = mark[2], date_of = mark[3])
        session.add(mark2add)
    
    session.commit()
