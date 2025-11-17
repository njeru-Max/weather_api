import requests

API_KEY = "a3770c7a8994db676d641b4827f57d7d"  # your key
CITY = "Nairobi"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    print("✅ Success! Weather data:")
    print(data)
else:
    print("❌ Error:", response.status_code, response.text)
