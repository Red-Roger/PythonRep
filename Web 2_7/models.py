from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

class Groups(Base):
    __tablename__ = "groups"
    group_name = Column(Integer, primary_key=True)

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey(Groups.group_name, ondelete="CASCADE"))

class Tutors(Base):
    __tablename__ = "tutors"
    id = Column(Integer, primary_key=True)
    tutor_name = Column(String(50), nullable=False)

class Lessons(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True)
    lesson = Column(String(50), nullable=False)
    tutor_id = Column(Integer, ForeignKey(Tutors.id, ondelete="CASCADE"))

class Marks(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(Students.id, ondelete="CASCADE"))
    lesson_id = Column(Integer, ForeignKey(Lessons.id, ondelete="CASCADE"))
    rate = Column(Integer)
    date_of = Column(DateTime)

