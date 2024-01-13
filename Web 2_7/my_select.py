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

print (select_3())
