#!/usr/bin/python3
"""
Task 2: Filter states by user input
Write a script that takes in an argument and displays all values in
the 'states' table of hbtn_0e_0_usa where 'name' matches the argument
"""

import MySQLdb
import sys

if __name__ == '__main__':
    server = "localhost"
    user = sys.argv[1]
    passw = sys.argv[2]
    dbname = sys.argv[3]
    stateparam = sys.argv[4]

    db = MySQLdb.connect(server, user, passw, dbname)

    cursor = db.cursor()

    sql = "SELECT * FROM states \
            WHERE name = '{}' ORDER BY id ASC;".format(stateparam)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("***Cant Execute***")

    db.close()
