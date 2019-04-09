import Main
import sqlite3


def init(conn):
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE if not exists launchPaths
                 (id INTEGER PRIMARY KEY ASC, name text, path text)''')

    add_launcher(conn, 'Steam', 0)
    add_launcher(conn, 'Origin', 1)

    conn.commit()


def add_launcher(conn, name, row_id):
    c = conn.cursor()
    temp = (name, )
    sql = '''SELECT * FROM launchPaths WHERE name = ?'''
    c.execute(sql, temp)

    results = c.fetchall()
    sql = "INSERT INTO launchPaths VALUES (?, ?, 'NullPath')"
    if len(results) == 0:
        c.execute(sql, (row_id, name))

    conn.commit()


if __name__ == '__main__':
    init()
