@echo off
cd C:\weather_pipeline
call venv\Scripts\activate
python elt.py
streamlit run app_streamlit.py
pause
