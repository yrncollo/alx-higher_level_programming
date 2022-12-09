#!/usr/bin/python3
"""
model_city module
model_city module supplies City class definition and an instance
    Base = declarative_base()
"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """
        Class City
        Linked to the MySQL table cities

        **class attributes**
         id: auto-generated, unique integer, can't be null and is a primary key
         name: string with maximum 128 characters and can't be null
         state_id: integer, can't be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
