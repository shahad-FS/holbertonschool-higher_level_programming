#!/usr/bin/python3
"""
Print the first State object from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create SQLAlchemy engine to connect to the MySQL database
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ),
            pool_pre_ping=True
            )

    # Create a configured "Session" Class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the first State object by id (asc order)
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
