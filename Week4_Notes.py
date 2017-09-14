import sqlite3

#create / connect to DB
conn = sqlite3.connect('Many2Many.sqlite')

#cursor (file handler for the DB file)
cur = conn.cursor()

#Starts anew each time to don't have double entry / bad entries
cur.executescript('''
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;''')

cur.execute('''CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    email TEXT
    );''')

cur.execute('''CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT
    );''')

cur.execute('''CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role integer,
    PRIMARY KEY (user_id, course_id)
    );''')
cur.executescript('''
INSERT INTO User (name, email) VALUES ('Jane', 'jane@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO User (name, email) VALUES ('Sue', 'sue@tsugi.org');

INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');
''')
