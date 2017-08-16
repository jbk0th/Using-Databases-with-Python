import sqlite3
    #creates if does not exist database for tracks
conn = sqlite3.connect('Trackdb.sqlite')
    #establishes connection to the database
cur = conn.cursor()
    # creates the table 'Artist' id key autoincrements and must be unique, the artists name is stored there and will be referenced by table downstream
cur.execute(''' CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );''')

cur.execute(''' CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );''') # each line starts with the name of the prospective column followed by the schema thats being set for it entries
    #
cur.execute(''' CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
    );''')
cur.execute(''' CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
    );''')
