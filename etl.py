import requests
import sqlite3
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
CITIES = ["Karachi", "Lahore", "Islamabad", "London", "New York"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def insert_weather(city, temp, humidity, desc):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity REAL,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute(
        "INSERT INTO weather_data (city, temperature, humidity, description) VALUES (?, ?, ?, ?)",
        (city, temp, humidity, desc)
    )
    conn.commit()
    conn.close()

for city in CITIES:
    data = fetch_weather(city)

    # ✅ Safety check
    if "main" in data and "weather" in data:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]

        insert_weather(city, temp, humidity, desc)
        print(f"✅ {city} inserted: {temp}°C, {humidity}% humidity, {desc}")
    else:
        print(f"⚠️ Skipped {city} — Invalid response: {json.dumps(data, indent=2)}")
