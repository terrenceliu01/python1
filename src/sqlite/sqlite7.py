import sqlite3
from sqlite2 import *
"""
Create relational data table by using primary key and foriener key fields
"""

if __name__ == '__main__':
    database = "pythonsqlite.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        projects = [
            (111, 'project-111', '2020-03-28', '2020-04-28'),
            (222, 'project-222', '2020-05-01', '2020-08-31'),
            (333, 'project-333', '2020-07-06', '2020-07-30'),
        ]
        c.executemany('INSERT INTO projects VALUES (?,?,?,?)', projects)
        conn.commit()
        tasks = [
            (11101, 'task-111-1', 10, 111, '2020-03-28', '2020-04-28'),
            (22202, 'task-111-2', 5, 111, '2020-04-01', '2020-04-10'),
            (33303, 'task-111-3', 5, 111, '2020-04-10', '2020-04-15'),
        ]
        c.executemany('INSERT INTO tasks VALUES (?,?,?,?,?,?)', tasks)
        # the following is very important statement, otherwise no data will be stored into database
        conn.commit()
        tasks = [
            (11104, 'task-222-4', 5, 222, '2020-05-28', '2020-05-28'),
            (22205, 'task-222-5', 9, 222, '2020-05-01', '2020-05-10'),
            (33306, 'task-222-6', 9, 222, '2020-05-10', '2020-08-15'),
        ]
        c.executemany('INSERT INTO tasks VALUES (?,?,?,?,?,?)', tasks)
        # the following is very important statement, otherwise no data will be stored into database
        conn.commit()
        tasks = [
            (11107, 'task-333-7', 5, 333, '2020-04-10', '2020-04-12'),
            (22208, 'task-333-8', 9, 333, '2020-04-13', '2020-04-14'),
            (33309, 'task-333-9', 9, 333, '2020-05-15', '2020-04-15'),
        ]
        c.executemany('INSERT INTO tasks VALUES (?,?,?,?,?,?)', tasks)
        # the following is very important statement, otherwise no data will be stored into database
        conn.commit()
    except Exception as error:
        print("Error:", error)
    conn.close()
    print("Done.")
