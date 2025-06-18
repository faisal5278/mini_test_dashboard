
import sqlite3


conn = sqlite3.connect('test_data.db')
cursor = conn.cursor()


with open('schema.sql', 'r') as f:
    schema = f.read()
    cursor.executescript(schema)

print("Database created successfully!!!")

conn.commit()
conn.close()
