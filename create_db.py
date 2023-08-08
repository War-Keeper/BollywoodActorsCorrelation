import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



if __name__ == '__main__':

    database = "bolly.db"
    

    sql_create_actors_table = """ CREATE TABLE IF NOT EXISTS actors (
                                        name text PRIMARY KEY,
                                        total_movies text NOT NULL
                                    ); """

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    project_id integer NOT NULL,
                                    project_name text NOT NULL,
                                    actor_name REFERENCES actors(name)
                                );"""
    
    conn = create_connection(database)
    conn.execute("PRAGMA foreign_keys = ON")

    if conn is not None:
        # create projects table
        create_table(conn, sql_create_actors_table)

        # create tasks table
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")