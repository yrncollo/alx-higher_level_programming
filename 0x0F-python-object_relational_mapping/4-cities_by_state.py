#!/usr/bin/python3
"""
Python script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("""
                      SELECT cities.id, cities.name, states.name
                        FROM cities
                        LEFT JOIN states
                          ON cities.state_id = states.id
                       ORDER BY cities.id ASC;
                    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
