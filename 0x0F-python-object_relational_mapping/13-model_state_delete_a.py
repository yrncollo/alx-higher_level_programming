#!/usr/bin/python3
"""
Python script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
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

    """ extract states """
    result = session.query(State).filter(State.name.like('%a%'))
    for r in result:
        session.delete(r)

    """ commit session and end session """
    session.commit()
    session.close()
    engine.dispose()
