#!/usr/bin/python3
""" This module uses MySQLdb to print out states

Usage:
    ./filename user pw db
"""


import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    dt = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        passwd=args[2],
        db=args[3],
        charset="utf8")
    cursor = dt.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                   JOIN states ON cities.state_id = states.id ORDER \
                   BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dt.close()
