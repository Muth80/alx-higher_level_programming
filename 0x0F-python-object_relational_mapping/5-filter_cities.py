#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Prepare the SQL query with placeholders for state name
    query = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the SQL query with the state name as the parameter
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Print the result
    print(result)

    # Close the cursor and database connection
    cursor.close()
    db.close()

