#!/usr/bin/python3

""" A script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)

    new_cursor = db.cursor()
    new_cursor.execute('SELECT * FROM states;')
    states = new_cursor.fetchall()

    for state in states:
        print(state)
