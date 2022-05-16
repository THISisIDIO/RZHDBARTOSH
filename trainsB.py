import sqlite3

def create_tables():
    conn = sqlite3.connect('railways.db')
    conn.execute('''CREATE TABLE locomotive_types
            (
            locomotive_type_id INTEGER PRIMARY KEY NOT NULL,
            type_name TEXT NOT NULL
            );''')
    conn.commit()
    conn.close()  

