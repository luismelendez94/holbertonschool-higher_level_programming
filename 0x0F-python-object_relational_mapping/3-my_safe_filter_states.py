#!/usr/bin/python3
"""
Task 3: SQL Injection...
Write a script that takes in arguments and displays all values in
the 'states' table of hbtn_0e_0_usa where 'name' matches the argument.
But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == '__main__':
    server = "localhost"
    user = sys.argv[1]
    passw = sys.argv[2]
    dbname = sys.argv[3]
    stateparam = sys.argv[4].split(" ")

    db = MySQLdb.connect(server, user, passw, dbname)

    cursor = db.cursor()

    sql = "SELECT * FROM states \
            WHERE name LIKE BINARY '{}' ORDER BY id ASC;".format(stateparam[0])

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("***Cant Execute***")

    db.close()
