import sqlite3

conn = sqlite3.connect('project.db')
cursor = conn.cursor()

def get_db():
    conn = sqlite3.connect('project.db')
    conn.row_factory = sqlite3.Row
    return conn

# create statement for the sites table 
cursor.execute('''CREATE TABLE IF NOT EXISTS sites (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               location TEXT NOT NULL,
               region TEXT NOT NULL,
               site_type TEXT NOT NULL CHECK(site_type IN ('tower', 'data_center', 'switch', 'router'))
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS incidents (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               description TEXT NOT NULL,
               severity TEXT NOT NULL CHECK(severity IN ('low', 'medium', 'high', 'critical')),
               status TEXT NOT NULL CHECK(status IN ('open', 'resolved', 'in_progress')),
               site_id INTEGER NOT NULL,
               created_at TEXT NOT NULL DEFAULT (datetime('now')),
               resolved_at TEXT,
               FOREIGN KEY(site_id) REFERENCES sites(id)
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS updates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                update_text TEXT NOT NULL,
                updated_by TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                incident_id INTEGER NOT NULL,
                FOREIGN KEY(incident_id) REFERENCES incidents(id)
                 )''')


conn.commit()
conn.close()

print("Database and tables created successfully.")
