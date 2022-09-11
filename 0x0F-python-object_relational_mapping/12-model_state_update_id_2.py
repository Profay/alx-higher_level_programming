#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from sqlalchemy import text


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    searchName = 2
    row = session.query(State).order_by(State.id).\
        filter(text("id=:value")).params(value=searchName).first()
    row.name = 'New Mexico'
    session.commit()
    session.close()
