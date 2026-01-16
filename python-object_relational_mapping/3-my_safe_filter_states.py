#!/usr/bin/python3
"""
Lists states from the database where name matches the argument.
This version is safe from SQL injection
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database
            )

    # Create cursor object to execute SQL queries
    cursor = db.cursor()

    # SQL query using parameterized query (safe from SQL injection)
    query = "SELECT id, name FROM states WHERE BINARY name = %s ORDER BY id ASC"

    # Execute the query with user input salfly passed as parameter
    cursor.excute(query, (stat_name,))

    # Fetch and print all matching rows
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection 
    cursor.close()
    db.close()
