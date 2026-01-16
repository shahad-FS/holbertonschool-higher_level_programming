#!/usr/bin/python3
"""
List all State object that contains letter 'a'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Ensure 3 arguments: username, password, database
    if len(sys.argv) != 4:
        sys.exit(1)

    # Get the cridentials from the command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                username, password, database),
            pool_pre_ping=True
            )

    # Bind a session to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing 'a'
    states = session.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
