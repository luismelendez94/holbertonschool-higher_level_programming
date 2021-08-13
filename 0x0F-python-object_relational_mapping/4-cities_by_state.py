#!/usr/bin/python3
"""
Task 4: Cities by states
Write a script that lists all 'cities' from database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    server = "localhost"
    user = sys.argv[1]
    passw = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(server, user, passw, dbname)

    cursor = db.cursor()

    sql = "SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC;"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("***Cant Execute***")

    db.close()
