from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///Web 2_7/courses.db")

Session = sessionmaker(bind=engine)
session = Session()