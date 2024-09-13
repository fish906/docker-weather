import os
import requests
import logging
from flask import Flask, render_template, abort

# Setup logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Fetch weather data function
def get_weather_data():
    api_key = os.getenv("WEATHER_API_KEY")
    city_id = os.getenv("CITY_ID")
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        abort(500)  # Return a 500 Internal Server Error response

# Fetch forecast data function
def get_forecast_data():
    api_key = os.getenv("WEATHER_API_KEY")
    city_id = os.getenv("CITY_ID")
    url = f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={api_key}&units=metric&cnt=16"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching forecast data: {e}")
        return None

@app.route("/")
def index():
    weather_data = get_weather_data()
    forecast_data = get_forecast_data()

    if weather_data is None or forecast_data is None:
        abort(500, description="Unable to retrieve weather data at the moment.")

    radar_lat = os.getenv("RADAR_LAT")
    radar_lon = os.getenv("RADAR_LON")
    return render_template("index.html", weather=weather_data, forecast=forecast_data, radar_lat=radar_lat, radar_lon=radar_lon)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)