#!/usr/bin/python3
"""
model_state module
model_state module supplies State class definition and an instance
    Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """
        Class State
        Linked to the MySQL table states

        **class attributes**
         id: auto-generated, unique integer, can't be null and is a primary key
         name: string with maximum 128 characters and can't be null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
