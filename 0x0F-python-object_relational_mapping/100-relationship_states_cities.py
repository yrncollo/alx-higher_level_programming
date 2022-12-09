#!/usr/bin/python3
"""
Python script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
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

    new_state = State(name="California")
    new_state.cities = [City(name="San Francisco")]
    session.add(new_state)
    session.commit()
    session.close()
    engine.dispose()
