#!/usr/bin/python3
"""
Task 1: Filter states
Write a script that lists all 'states' with a 'name'
starting with 'N' (upper N) from the database hbtn_0e_0_usa
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

    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("***Cant Execute***")

    db.close()
