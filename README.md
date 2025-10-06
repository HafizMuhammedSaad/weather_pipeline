# 🌤️ Weather Data Pipeline

This project fetches real-time weather data using OpenWeather API, stores it in SQLite, and automates the ETL process using **GitHub Actions** every 6 hours.

### Features:
- Automatic ETL via GitHub Actions
- Data stored in `weather_data.db`
- Streamlit dashboard for visualization

### Run locally:
```bash
pip install -r requirements.txt
python etl.py
