import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="🌦 Real-Time Weather Dashboard", layout="wide")

# Database connection
def load_data():
    conn = sqlite3.connect("weather_data.db")
    df = pd.read_sql_query("SELECT * FROM weather_data", conn)
    conn.close()
    return df

st.title("🌦 Real-Time Weather Data Dashboard")

# Load data
df = load_data()

if df.empty:
    st.warning("No data found. Please run 'elt.py' first to fetch weather data.")
else:
    # Layout with columns
    col1, col2, col3 = st.columns(3)

    # Analytics metrics
    hottest_city = df.loc[df['temperature'].idxmax()]
    coldest_city = df.loc[df['temperature'].idxmin()]
    avg_temp = round(df['temperature'].mean(), 2)

    col1.metric("🔥 Hottest City", hottest_city['city'], f"{hottest_city['temperature']}°C")
    col2.metric("❄️ Coldest City", coldest_city['city'], f"{coldest_city['temperature']}°C")
    col3.metric("🌍 Avg Temperature", f"{avg_temp}°C")

    st.divider()

    # Trend chart
    st.subheader("📈 Temperature Trends Over Time")
    fig = px.line(df, x="timestamp", y="temperature", color="city", title="City-wise Temperature Trends")
    st.plotly_chart(fig, use_container_width=True)

    # Average temperature by city
    st.subheader("🏙 Average Temperature per City")
    avg_df = df.groupby('city')['temperature'].mean().reset_index()
    fig2 = px.bar(avg_df, x='city', y='temperature', color='city', title="Average Temperature by City")
    st.plotly_chart(fig2, use_container_width=True)

    # Show raw data
    with st.expander("📊 Show Raw Data"):
        st.dataframe(df)
