import sqlite3
import Initialize


def main():
    conn = sqlite3.connect('main_database.db')
    c = conn.cursor()
    Initialize.init(conn)

    print("print rows")
    get_launch_paths(c)

    update_path(conn, 'Steam', "C:\\Program Files (x86)\Steam\\steamapps\\common")
    update_path(conn, 'Origin', "C:\\Program Files(x86)\\Origin Games")
    get_launch_paths(c)
    conn.close()


def update_path(conn, name, path):
    c = conn.cursor()
    sql = ''' UPDATE launchPaths
                  SET path = ? 
                  WHERE name = ?'''
    c.execute(sql, (path, name))
    conn.commit()


def get_launch_paths(cursor):
    for row in cursor.execute('SELECT * FROM launchPaths'):
        print(row)


if __name__ == '__main__':
    main()

