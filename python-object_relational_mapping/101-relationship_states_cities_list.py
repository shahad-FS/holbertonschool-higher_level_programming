#!/usr/bin/python3
"""
Lists all State objects, and corresponding City object
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":
    # Ensure 3 arguments: username, password, database
    if len(sys.argv) != 4:
        sys.exit(1)

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

    # Query all states with thier cities in one go
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")
        # Print each city of the state, order by city.id
        for city in stored(state.cities, key=lambda c: c.id):
            print(f"    {city.id}: {city.name}")

    # Close session
    session.close()
