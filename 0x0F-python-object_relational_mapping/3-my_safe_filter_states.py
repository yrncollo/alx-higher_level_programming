#!/usr/bin/python3
"""
Python script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument and is safe from MySQL
injections!
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
                       WHERE name = %s
                       ORDER BY id ASC;
                   """,
                   (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
