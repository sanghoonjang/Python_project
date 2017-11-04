
import sqlite3

# make file.db
conn = sqlite3.connect('example.db')

c = conn.cousor()

c.execute('''CREATE TABLE items ()''')

c.execute("INSERT INTO items VALUES ()")

conn.commit()
conn.close()

c.execute('SELECT * FROM items ORDER BY price')

