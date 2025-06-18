
import sqlite3
import json

conn = sqlite3.connect('test_data.db')
cursor = conn.cursor()


with open('sample_data.json', 'r') as f:
    test_data = json.load(f)


for test in test_data:
    cursor.execute('''
        INSERT INTO test_results (test_name, status, module, duration, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        test['test_name'],
        test['status'],
        test['module'],
        test['duration'],
        test['timestamp']
    ))

print("Sample test data inserted successfully!!!")

conn.commit()
conn.close()
