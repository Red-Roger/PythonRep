from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from connect_db import session

import argparse
from connect_db import session
from models import Groups, Students, Tutors, Lessons, Marks


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", nargs=1, action = "store", help="Action whith records")
parser.add_argument("-m", "--modify", nargs=1, action = "store", help="Table to modify")
parser.add_argument("-n", "--name", nargs=1, action = "store", help="Name to add")
parser.add_argument("--id", action = "store", help="ID")
args = parser.parse_args()
if args.action:
    if args.action[0]  == 'list':

        if args.modify[0] == 'Tutors':
            q = session.query(Tutors.tutor_name)\
                .select_from(Tutors).all()
            print (q)
        if args.modify[0] == 'Groups':
            q = session.query(Groups.group_name)\
                .select_from(Groups).all()
            print (q)  
        if args.modify[0] == 'Students':
            q = session.query(Students.student_name)\
                .select_from(Students).all()
            print (q)

    if args.action[0]  == 'create':

        if args.modify[0] == 'Tutors':
            if args.name:
                tutor2add = Tutors(tutor_name=args.name[0])
                session.add(tutor2add)
        if args.modify[0] == 'Group':
            if args.name:
                groups2add = Groups(group_name=args.name[0])
                session.add(groups2add)

    if args.action[0]  == 'delete':
        if args.modify[0] == 'Tutors':
            if args.id:
                session.query(Tutors).filter(Tutors.id == args.id).delete()
        
            if args.modify[0] == 'Students':
                if args.id:
                    session.query(Students).filter(Students.id == args.id).delete()

session.commit()

