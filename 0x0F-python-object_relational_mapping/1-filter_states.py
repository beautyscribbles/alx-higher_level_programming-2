#!/usr/bin/python3
"""
File: 1filter_states.py
Author Florence Hanson
Desc: A script_that_lists_states with_a_name starting_with N
        from_the_database hbtn_0e_0_usa.
Date: 19_ December_2023
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                    WHERE BINARY name LIKE 'N%' ORDER BY id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
