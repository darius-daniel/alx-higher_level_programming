#!/usr/bin/python3
"""
A script that prints the first State Object from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from model_state import States, Base
import sys

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    if session.query(States).count() == 0:
        print()
    else:
        state = session.query(States).order_by(id).first()
        print("{}: {}".format(state.id, state.name))
