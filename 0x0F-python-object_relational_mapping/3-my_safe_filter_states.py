#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name is matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cursor = db.cursor()
    name = sys.argv[4].split(';')[0].strip("'")
    cursor.execute(f"SELECT * FROM states WHERE name='{name}'")
    states = cursor.fetchall()

    for state in states:
        print(state)
