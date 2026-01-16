#!/usr/bin/python3
"""
Lists all cities of a given state from the database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database,
            )

    # Create cursor object
    cursor = db.cursor()

    # SQL query to fetch city names for the given state safly
    query = """
    SELECT cities.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the query safely using parameterized input
    cursor.execute(query, (state_name,))

    # Fethc all city names
    cities = [row[0] for row in cursor.fetchall()]

    # Print cities separated by commas
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close()
