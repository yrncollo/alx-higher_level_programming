#!/usr/bin/python3
"""
Python script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_url)

    """ generate database schema """
    Base.metadata.create_all(engine)

    """ create a new session """
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).all()
    for state in results:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
    engine.dispose()
