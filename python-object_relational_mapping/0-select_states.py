#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database
            )

    # create cursor
    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch and print result
    for row in cursor.fetchall():
        print(row)

    # close cursor and connection
    cursor.close()
    db.close()
