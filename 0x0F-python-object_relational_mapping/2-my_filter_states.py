#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
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
        f"SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_CS LIKE '{sys.argv[4]}'"
    )
    states = cursor.fetchall()

    for state in states:
        print(state)
