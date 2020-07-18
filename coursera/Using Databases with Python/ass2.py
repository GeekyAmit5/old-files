import sqlite3

conn = sqlite3.connect('coursera/Using Databases with Python/ass2.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fh = open('coursera/Using Databases with Python/mbox.txt')
for line in fh:
    if not line.startswith('From:'):
        continue
    pieces = line.split()
    org = pieces[1].split("@")[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
        conn.commit()
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 5'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
