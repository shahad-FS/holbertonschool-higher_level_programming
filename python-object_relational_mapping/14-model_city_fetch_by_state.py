#!/usr/bin/python3
"""
Lists all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Ensure 3 arguments: username, password, database
    if len(sys.argv) != 4:
        sys.exit(1)

    # Get the cridentials from command-line arguments
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

    # Query all cities joined with their states, stored by city id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # print out the state and city name and id
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
