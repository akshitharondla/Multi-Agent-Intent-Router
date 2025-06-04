# Shared Memory (SQLite for simplicity)
import json, sqlite3, os

class Memory:
    def __init__(self):
        self.db_path = 'logs/memory.db'
        self.init_db()

    def init_db(self):
        os.makedirs('logs', exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY AUTOINCREMENT, source TEXT, format TEXT, intent TEXT, data TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

    def log(self, source, format_type, intent):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO memory (source, format, intent) VALUES (?, ?, ?)', (source, format_type, intent))
        conn.commit()
        conn.close()

    def store_data(self, source_type, data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO memory (source, format, intent, data) VALUES (?, ?, ?, ?)', (source_type, 'structured', 'Parsed', json.dumps(data)))
        conn.commit()
        conn.close()
