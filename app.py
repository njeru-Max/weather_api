1
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Load API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY",)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"].title(),
                "icon": data["weather"][0]["icon"],
            }
        else:
            weather_data = {"error": "City not found!"}

    return render_template("index.html", weather=weather_data)


@app.route("/offline")
def offline():
    """Offline fallback page for PWA."""
    return render_template("offline.html")


@app.route("/weather/<city>")
def get_weather(city: str):
    """Fetch weather data for a given city (used for AJAX/JS calls)."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}  
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"],
        }
        return jsonify(weather)
    else:
        return jsonify({"error": response.json()}), response.status_code


if __name__ == "__main__":
    # Debug=True reloads the app automatically when you save changes
    app.run(debug=True)
