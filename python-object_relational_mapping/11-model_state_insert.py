#!/user/bin/python3
"""
Add the State object "Louisiana" to the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Ensure 3 arguments: username, password, database
    if len(sys.argv) =! 4:
        sys.exit(1)

    username, password, database = (
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
            )

    # Create engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                username, password, database),
            pool_pre_ping=True
            )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new state object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Cloes session
    session.close()
