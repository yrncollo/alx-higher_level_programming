#!/usr/bin/python3
"""
Python script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument though not safe from
SQL injection. i.e.
./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona';
TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("""
                      SELECT *
                        FROM states
                       WHERE name LIKE BINARY '{:s}'
                       ORDER BY id ASC;
                   """
                   .format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
