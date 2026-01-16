#!/usr/bin/python3
"""
Changes the name of the State with id = 2 to "New Mexico"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Ensure 3 arguments: username, password, database
    if len(sys.argv) != 4:
        sys.exit(1)

    # Get the credintials from the command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                username, password, database),
            pool_pre_ping=True
            )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the state with id = 2
    state = session.query(State).get(2)

    # Update the name if the state exists
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
