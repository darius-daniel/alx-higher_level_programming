#!/usr/bin/python3
"""
A script that prints the first State Object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(State).count() == 0:
        print('Nothing')
    else:
        state = session.query(State).first()
        print("{}: {}".format(state.id, state.name))
