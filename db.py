import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('DROP TABLE IF EXISTS mappingTable;')
conn.execute('CREATE TABLE mappingTable (id INTEGER PRIMARY KEY, fail_code TEXT, '
             'component TEXT, fail_mode TEXT, component_id TEXT, fail_mode_id TEXT)')

conn.execute('DROP TABLE IF EXISTS failModesTable;')
conn.execute('CREATE TABLE failModesTable (id INTEGER PRIMARY KEY, name TEXT, code TEXT)')

conn.execute('DROP TABLE IF EXISTS componentTable;')
conn.execute('CREATE TABLE componentTable (id INTEGER PRIMARY KEY, name TEXT, contact TEXT, manufacturer TEXT,'
             'failure_rate FLOAT, price FLOAT, quantity INTEGER)')

conn.close()
