#!/usr/bin/python3
"""
A script that lists all states from a database (hbtn_0e_0_usa)
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM hbtn_0e_0_usa.states")
    states = cursor.fetchall()

    for state in states:
        print(state)
