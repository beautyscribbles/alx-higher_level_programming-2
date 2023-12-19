#!/usr/bin/python3
""" List_all_the_states from_the_database hbtn_0e_0_usa."""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
