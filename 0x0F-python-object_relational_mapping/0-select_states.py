#!/usr/bin/python3
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor:
        print(row)
    cursor.close()
    dt.close()
