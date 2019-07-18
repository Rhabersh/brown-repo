import sqlite3
from sqlite3 import Error


def sqlite_connect():

    try:
        sqlite_con = sqlite3.connect('slurm_database.db')
        print 'Connection valid - Database active'
        return sqlite_con

    except Error:
        print Error


def create_table(sqlite_con):
    py_cursor = sqlite_con.cursor()
    py_cursor.execute('CREATE TABLE resources(jobID integer PRIMARY KEY, memory integer, cores integer, time integer)')
    sqlite_con.commit()


def insert_data(sqlite_con, ph):
    py_cursor = sqlite_con.cursor()
    py_cursor.execute('INSERT INTO resources(jobID, memory, cores, time) VALUES(?, ?, ?, ?)', ph)
    sqlite_con.commit()


con = sqlite_connect()
# create_table(con)

ph = (0, 0, 0, 0,)
insert_data(con, ph)
