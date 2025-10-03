import requests
import sqlite3

API_KEY = "df10c03c6e42739d26fdb6195368693e"   # apna API key daalo
CITIES = ["Karachi", "Lahore", "Islamabad", "London", "New York"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def insert_weather(city, temp, humidity, desc):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO weather (city, temperature, humidity, description) VALUES (?, ?, ?, ?)",
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

API_KEY = "df10c03c6e42739d26fdb6195368693e"   # apna API key daalo
CITIES = ["Karachi", "Lahore", "Islamabad", "London", "New York"]

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def insert_weather(city, temp, humidity, desc):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO weather (city, temperature, humidity, description) VALUES (?, ?, ?, ?)",
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
