#!/usr/bin/python3
"""This script defines a City class to work with MySQLAlchemy ORM.
City class: inherits from Base (imported from model_state)
           links to the MySQL table cities
class attribute id that represents a column of an auto-generated, unique \
integer, can’t be null and is a primary key.
class attribute name that represents a column of a string of 128 characters\
 and can’t be null
class attribute state_id that represents a column of an integer, can’t be \
null and is a foreign key to states.id
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
