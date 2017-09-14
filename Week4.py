import sqlite3
import json

conn = sqlite3.connect('Roster_DB.sqlite')
# file hangle analog for the DB
cur = conn.cursor()
# filename going to use
fn = 'roster_data.json'
# file handle use to access particular file
fh = open(fn)
# read(), with fi handle reads all data in as string, then load serialize
# the string into JSON doc, if data being serialized, NOT valid json
# doc JSONDecodeError thrown

data = json.loads(fh.read())
#json_str = json.dumps(data, indent=4, sort_keys=True)

input('Pause\n')

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;''')

cur.execute('''CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
    );''')

cur.execute('''CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT
    );''')

cur.execute('''CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
    );''')

for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print(name, title, role)
# insert the name into the User table
    cur.execute('''INSERT or IGNORE INTO User (name) VALUES (?)''', ( name, ) )
# the queries the table for the user name that was just put in the 'fetches' it,
# which info comes back as a tuple, which its info
# can then be selected by indexing like any tuple for the desired info at that spot
    cur.execute('''SELECT id FROM User WHERE name = ?''', ( name, ) )
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', ( title, ) )

    cur.execute('''SELECT id FROM Course WHERE title = ?''', ( title, ) )
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Member (user_id, course_id, role)
                VALUES (?, ?, ?)''', (user_id, course_id, role) )
conn.commit()
