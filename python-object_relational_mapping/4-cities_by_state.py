#!/usr/bin/python3
"""
Lists all cities from the database along with their corresponding state.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database
            )

    # Create cursor object
    cursor = db.cursor()

    # SQL query to fetch cities and their states
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON cities.state_id = state.id
    ORDER BY cities.id ASC
    """

    # Execute the query
    cursor.execute(query)

    # Fetch and print all result
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
