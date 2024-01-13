from connect_db import session
from sqlalchemy import desc, asc, func
from models import Groups, Students, Tutors, Lessons, Marks

def select_1():
    q = session.query(Students.student_name, func.round(func.avg(Marks.rate), 2).label('avg_rate'))\
            .select_from(Students, Marks).where(Marks.student_id == Students.id).group_by(Students.student_name).order_by(desc('avg_rate')).limit(5).all()
    return q

def select_2():
    q = session.query(Lessons.lesson, Students.student_name, func.max(Marks.rate).label('max_rate'))\
            .select_from(Marks).join(Students).join(Lessons).group_by(Lessons.lesson).order_by(asc('lesson')).all()
    return q

def select_3():
    q = session.query(Students.group_id, Lessons.lesson, func.round(func.avg(Marks.rate), 2).label('avg_rate'))\
            .select_from(Students).join(Marks).join(Lessons).group_by(Students.group_id, Lessons.lesson).order_by(asc('lesson')).all()
    return q

def select_4():
    q = session.query(func.round(func.avg(Marks.rate), 2).label('avg_rate'))\
            .select_from(Marks).all()
    return q

def select_5():
    q = session.query(Tutors.tutor_name, Lessons.lesson)\
            .select_from(Tutors).join(Lessons).order_by('tutor_name').all()
    return q

def select_6():
    q = session.query(Students.group_id, Students.student_name)\
            .select_from(Students).where(Students.group_id == 2).all()
    return q

def select_7():
    q = session.query(Students.group_id, Lessons.lesson, Students.student_name, Marks.rate)\
            .select_from(Students).join(Marks).join(Lessons).where(Students.group_id == 2).where(Lessons.id == 3).order_by('group_id','lesson').all()
    return q

def select_8():
    q = session.query(Lessons.lesson, Tutors.tutor_name, func.round(func.avg(Marks.rate), 2).label('avg_rate'))\
            .select_from(Marks).join(Lessons).join(Tutors).group_by(Tutors.tutor_name, Marks.lesson_id).order_by('lesson').all()
    return q

def select_9():
    q = session.query(Students.student_name, Lessons.lesson)\
            .select_from(Marks).join(Lessons).join(Students).where(Students.id == 46).all()
    return q

def select_10():
    q = session.query(Tutors.tutor_name, Students.student_name, Lessons.lesson)\
            .select_from(Students).join(Marks).join(Lessons).join(Tutors).where(Marks.student_id == 37).where(Lessons.tutor_id == 1).all()
    return q

def select_11():
    q = session.query(Tutors.tutor_name, Students.student_name, func.round(func.avg(Marks.rate), 2).label('avg_rate'))\
            .select_from(Students).join(Marks).join(Lessons).join(Tutors).where(Marks.student_id == 37).where(Lessons.tutor_id == 1).group_by(Tutors.tutor_name, Students.student_name).all()
    return q

def select_12():
    q = session.query(Students.group_id, Lessons.lesson, Students.student_name, Marks.rate, func.max(Marks.date_of).label('date'))\
            .select_from(Lessons).join(Marks).join(Students).where(Students.group_id == 1).where(Lessons.id == 2).group_by(Students.group_id, Lessons.lesson, Students.student_name, Marks.rate).all()
    return q


print (select_12())

