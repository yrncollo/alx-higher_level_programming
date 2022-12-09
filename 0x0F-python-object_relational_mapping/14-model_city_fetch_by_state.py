#!/usr/bin/python3
"""
Python script that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_url, pool_pre_ping=True)

    """ generate database schema """
    Base.metadata.create_all(engine)

    """ create a new session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ extract states """
    result = session.query(State.name, City.id, City.name).filter(
                           State.id == City.state_id).order_by(City.id)
    for r in result:
        print(f"{r[0]}: ({r[1]}) {r[2]}")

    session.close()
    engine.dispose()
