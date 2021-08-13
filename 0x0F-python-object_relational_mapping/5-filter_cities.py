#!/usr/bin/python3
"""
Task 5: All cities by state
Write a script that takes in the name of a state as an arument and lists all 'cities'
of that state, using the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    server = "localhost"
    user = sys.argv[1]
    passw = sys.argv[2]
    dbname = sys.argv[3]
    stateName = sys.argv[4].split(" ")

    db = MySQLdb.connect(server, user, passw, dbname)

    cursor = db.cursor()

    sql = "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY '{}'\
            ORDER BY cities.id ASC;".format(stateName[0])
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        citiesNames = ''
        for row in results:
            citiesName += row[1]
            citiesName += ", "
        print(citiesName[:-2])
    except:
        print("Cant connect")
        db.rollback

    db.close()
