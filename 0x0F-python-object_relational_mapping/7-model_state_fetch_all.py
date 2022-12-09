#!/usr/bin/python3
"""
Python script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_url, pool_pre_ping=True)

    """ generate database schema """
    Base.metadata.create_all(engine)

    """ create a new session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ extract all states """
    states = session.query(State.id, State.name).order_by(State.id)

    """ print states """
    for state in states:
        print(f"{state[0]}: {state[1]}")
    session.close()
    engine.dispose()
