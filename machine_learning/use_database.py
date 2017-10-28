
# SQLite
import sqlite3

# Access to database
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

# Set A Table AND Insert data
cur = conn.cursor()
cur.executescript("""

DROP DABLE IF EXISTS items;

CREATE TABLE items(
  item_id INTEGER PRIMARY KEY,
  name TEXT UNIQUE,
  price INTEGER
);

INSERT INTO items(name, price)VALUES("Apple", 800);
INSERT INTO items(name, price)VALUES("Orange", 700);
INSERT INTO items(name, price)VALUES("Banana", 430);
""")

conn.commit()

# Drag a data
cur = conn.cursor()
cur.execute("SELECT item_id,name,price FROM items")
item_list = cur.fetchall()

for it in item_list:
  print(it)

