import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print(sqlite3.version)

    except Error as e:
        print(e)
    return conn

def create_actor(conn, actor):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO actors(name,total_movies)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, actor)
    conn.commit()
    return cur.lastrowid

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(project_id,project_name,actor_name)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':

    database = "bolly.db"

    conn = create_connection(database)
    conn.execute("PRAGMA foreign_keys = ON")

    actor= ('Amitabh Bachchan', 50)
    actor_id= create_actor(conn, actor)

    project = (123,'testing', 'Amitabh Bachchan')
    project_id= create_project(conn, project)


