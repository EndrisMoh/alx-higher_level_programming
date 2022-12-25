#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
You must use the module SQLAlchemy
You must import State and Base from model_state
It connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Access to the database and get the states from the database."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
