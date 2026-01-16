#!/usr/bin/python3
"""
Print the State object with the name passed as argument
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import makesession
from model_state import Base, State

if __name__ == "__main__":
    # Ensure 4 arguments: username, password, database, state_name
    if len(sys.argv) != 5:
        sys.exit(1)

    # Get the credintials from the commind-line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2]\
            sys.argv[3], sys.argv[4]

    # Create the engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                username, password, database),
            pool_pre_ping=True
            )

    # Create and configured "Session" class and session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with given name (SQL injection safe)
    state = session.query(State).filter(State.name == state_name).first()

    # Print the results
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
