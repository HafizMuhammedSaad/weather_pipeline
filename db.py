import sqlite3

# DB connection
conn = sqlite3.connect("weather_data.db")
cursor = conn.cursor()

# Table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    description TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("✅ Database aur table successfully ban gaya!")
