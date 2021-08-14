#!/usr/bin/python3
"""
Task 7: All states via SQLAlchemy
Write a script that lists all 'State' objects from the database 'hbtn_0e_6_usa'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    user = sys.argv[1]
    pssw = sys.argv[2]
    dbnm = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, pssw, dbnm), pool_pre_ping=True)

    Session = sessionmaker(engine)
    mySession = Session()

    for state in mySession.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
