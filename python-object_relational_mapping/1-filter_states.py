#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username=sys.argv[1]
    password=sys.argv[2]
    database=sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database
            )

    # Create cursor
    cursor = MySQLdb.coursor()

    # Execute query
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
            )

    # Fetch and print result
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
