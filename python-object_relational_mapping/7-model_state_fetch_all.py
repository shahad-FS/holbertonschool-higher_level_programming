#!/usr/bin/python3
"""
Lists all state objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine to connect to MySQL
    engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
            pool_pre_ping=True
            )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create session
    session= Session()

    try:
        states = session.query(State).order_by(State.id).all()

        # Print the results
        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        # Close the session to free resources
        session.close()
