import requests
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
CITIES = ["Karachi", "Lahore", "Islamabad", "London", "New York"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def insert_weather(city, temp, humidity, desc):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weather_data (city, temperature, humidity, description) VALUES (?, ?, ?, ?)",
        (city, temp, humidity, desc)
    )
    conn.commit()
    conn.close()

for city in CITIES:
    data = fetch_weather(city)
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]

    insert_weather(city, temp, humidity, desc)
    print(f"✅ {city} inserted: {temp}°C, {humidity}% humidity, {desc}")
import requests
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
CITIES = ["Karachi", "Lahore", "Islamabad", "London", "New York"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def insert_weather(city, temp, humidity, desc):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO weather_data (city, temperature, humidity, description) VALUES (?, ?, ?, ?)",
        (city, temp, humidity, desc)
    )
    conn.commit()
    conn.close()

for city in CITIES:
    data = fetch_weather(city)
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desc = data["weather"][0]["description"]

    insert_weather(city, temp, humidity, desc)
    print(f"✅ {city} inserted: {temp}°C, {humidity}% humidity, {desc}")
