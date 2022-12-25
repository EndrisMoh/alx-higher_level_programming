#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
Use SQLAlchemy module & import State and Base from model_state
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        session.delete(instance)

    session.commit()
    session.close()
