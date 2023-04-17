#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

db = MySQLdb.connect(port=3306, user=sys.argv[1], passwd=sys.argv[2],
                     db=sys.argv[3])

current = db.cursor()
current.execute('SELECT * FROM states;')
states = current.fetchall()

for state in states:
    print(state)
