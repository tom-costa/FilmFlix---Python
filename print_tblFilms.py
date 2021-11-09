import sqlite3

conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()

for row in cursor.execute('SELECT * FROM tblFIlms'):
    print(row)