import sqlite3
from sqlite3 import Error


def sqlite_connect():
    """
        This function will use the sqlite3 module to connect to a database. If the
        specified database is not found in the local directory, a new one with
        the given name will be created.

        :return sqlite_con: The active d
    """
    try:
        sqlite_con = sqlite3.connect('slurm_database.db')
        print 'Connection valid - Database active'
        return sqlite_con

    except Error:
        print Error


def create_table(sqlite_con):
    """
        This function creates a table in the sqlite database and establishes the
        primary key as well as the other columns.

        :param sqlite_con: The active connection to the database is needed so this
                           function knows where to create/update the table.
        :return None:
    """
    py_cursor = sqlite_con.cursor()
    py_cursor.execute('CREATE TABLE resources(jobID integer PRIMARY KEY, memory integer, cores integer, time integer)')
    sqlite_con.commit()


def insert_data(sqlite_con, ph):
    """
        This function will insert the parsed data from pysqlite_parser into the table.

        :param sqlite_con: The active connection to the database.
        :param ph: Placeholder variable for when pysqlite_parser is actually finished.
                   Will be replaced by other variables for necessary fields.
        :return None:
    """
    py_cursor = sqlite_con.cursor()
    py_cursor.execute('INSERT INTO resources(jobID, memory, cores, time) VALUES(?, ?, ?, ?)', ph)
    sqlite_con.commit()


con = sqlite_connect()
# create_table(con)

ph = (0, 0, 0, 0,)
insert_data(con, ph)
