#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).join(City, State.id == City.state_id)
    states_and_cities = query.order_by(State.id.asc(), City.id.asc()).all()

    for state, cities in states_and_cities:
        print("{}: {}".format(state.id, state.name))
        for city in cities:
            print("{}{}: {}".format('\t', city.id, city.name))
