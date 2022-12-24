#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
It connect to a MySQL server running on localhost at port 3306
Use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = c.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    c.close()
    db.close()
