#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect(host='localhost:3306', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
db.curs