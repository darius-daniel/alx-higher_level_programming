#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper n) from a
database (hbtn_0e_0_usa
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
    cursor.execute(
        "SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_CS LIKE 'N%'"
    )
    states = cursor.fetchall()

    for state in states:
        print(state)
