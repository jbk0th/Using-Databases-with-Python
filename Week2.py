import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
	#connects to and creates a db file called emaildb
	#if does not already exists, itt creates one
cur = conn.cursor()
	# cursor to point at the db wish to manipulate, then can just send commands through it to the DB

cur.execute('''
DROP TABLE IF EXISTS Counts''')
	# delete the table if if exists / clean anything out of it
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
	# creates new table 'Counts' with schema email, text only entries and count only as an integer
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: '): continue
	pieces = line.split('@')
	org = pieces[1].strip()
	cur.execute('SELECT count FROM Counts WHERE org=? ', (org,))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
	else:
		cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
	
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()