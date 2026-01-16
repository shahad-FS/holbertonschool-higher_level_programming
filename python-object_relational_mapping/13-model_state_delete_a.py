#!/usr/bin/python3
"""
Delete all State object with a name containing the letter 'a'
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

    # Query all states containing 'a'
    states = session.query(State).filter(State.name.like("%a%")).all()

    # Delete them
    for state in states:
        session.delete(state)

    # Commit the changer
    session.commit()

    # Close session
    session.close()
