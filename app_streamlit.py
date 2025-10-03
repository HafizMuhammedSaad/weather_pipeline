import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import os

# DB fetch
def load_data():
    conn = sqlite3.connect("weather_data.db")
    df = pd.read_sql_query("SELECT * FROM weather", conn)
    conn.close()
    return df

st.set_page_config(page_title="🌦 Weather Dashboard", layout="wide")
st.title("🌦 Real-Time Weather Data Pipeline")

# 🔄 Refresh Button (ETL run)
if st.button("🔄 Refresh Data"):
    os.system("python etl.py")   
    st.rerun()    

df = load_data()

if df.empty:
    st.warning("⚠️ No data available yet. Run etl.py first!")
else:
    # ✅ Ensure required columns exist
    required_cols = ["city", "temperature", "humidity", "description", "timestamp"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = None   # default empty column

    # Last Updated
    last_updated = df["timestamp"].max()
    st.caption(f"🕒 Last Updated: {last_updated}")

    # Stats
    hottest = df.loc[df['temperature'].idxmax()]
    coldest = df.loc[df['temperature'].idxmin()]
    avg_temp = df['temperature'].mean()

    col1, col2, col3 = st.columns(3)
    col1.metric("🔥 Hottest City", hottest['city'], f"{hottest['temperature']}°C")
    col2.metric("❄️ Coldest City", coldest['city'], f"{coldest['temperature']}°C")
    col3.metric("🌍 Avg Temp", f"{avg_temp:.2f}°C")

    # Line chart (Temperature trends)
    st.subheader("🌡 Temperature Trends")
    fig_temp = px.line(df, x="timestamp", y="temperature", color="city", markers=True)
    st.plotly_chart(fig_temp, use_container_width=True)

    # Bar chart (Humidity comparison)
    st.subheader("💧 Humidity Comparison")
    fig_humidity = px.bar(df, x="city", y="humidity", color="city", barmode="group")
    st.plotly_chart(fig_humidity, use_container_width=True)

    # Latest Weather Details
    st.subheader("🌍 Latest Weather Details")
    st.dataframe(df[required_cols])

    # CSV Export Button
    st.download_button(
        label="📥 Download Data as CSV",
        data=df.to_csv(index=False),
        file_name="weather_data.csv",
        mime="text/csv"
    )
