#!/usr/bin/python3
"""
Display states matching the user input
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database
            )

    # Create cursor object to execute query
    cursor = db.cursor()

    # Build SQL query using format
    query = (
            "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
            ).format(state_name)

    # Execute SQL query
    cursor.execute(query)

    # Fetch and print all matching rows
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
