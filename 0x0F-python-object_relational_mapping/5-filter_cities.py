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
    newName = args[4]
    cursor = dt.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                   JOIN states ON cities.state_id = states.id \
                   WHERE states.name = %s ORDER \
                   BY cities.id ASC", (newName,))
    rows = cursor.fetchall()
    lisst = []
    for row in rows:
        lisst.append(row[0])
    print(", ".join(lisst))
    cursor.close()
    dt.close()
