#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and list all cities
of that state, using the database hbtn_0e_4_usa
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
        f"SELECT c.name FROM cities c \
            JOIN states s ON s.id = c.state_id \
                WHERE s.name='{sys.argv[4]}';"
    )
    cities = cursor.fetchall()

    for i in range(len(cities)):
        delimiter = ''
        city = str(cities[i]).strip("()'',")
        if i != len(cities) - 1:
            delimiter += ', '
        print(city, end=delimiter)
    print()
