from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
import os.path

if os.path.exists("Web 2_7/courses.db"):
    engine = create_engine("sqlite:///Web 2_7/courses.db")
elif os.path.exists("courses.db"):
    engine = create_engine("sqlite:///courses.db")
    
Session = sessionmaker(bind=engine)
session = Session()