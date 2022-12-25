#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
You must use the module SQLAlchemy
You must import State and Base from model_state
It connect to a MySQL server running on localhost at port 3306
The state you display must be the first in states.id
If the table states is empty, print Nothing followed by a new line
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Access to the database and get a state from the database."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
