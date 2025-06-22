import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching weather data. Check location and API key.")
        return None
    return response.json()

def check_conditions(weather_data, thresholds):
    alerts = []
    temp = weather_data['main']['temp']
    rain = weather_data.get('rain', {}).get('1h', 0)  # Rain volume in last 1 hour, mm
    wind_speed = weather_data['wind']['speed']

    if temp < thresholds['temp_min']:
        alerts.append(f"Temperature is below {thresholds['temp_min']}°F: currently {temp}°F")
    if temp > thresholds['temp_max']:
        alerts.append(f"Temperature is above {thresholds['temp_max']}°F: currently {temp}°F")
    if rain > thresholds['rain']:
        alerts.append(f"Rain detected: {rain} mm in last hour")
    if wind_speed > thresholds['wind']:
        alerts.append(f"High wind speed alert: {wind_speed} mph")

    return alerts

def main():
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    location = input("Enter city name or zip code: ").strip()
    
    print("Set your alert thresholds:")
    temp_min = float(input("Min temperature (°F) to alert if below: "))
    temp_max = float(input("Max temperature (°F) to alert if above: "))
    rain = float(input("Rainfall (mm) to alert if above: "))
    wind = float(input("Wind speed (mph) to alert if above: "))

    thresholds = {
        'temp_min': temp_min,
        'temp_max': temp_max,
        'rain': rain,
        'wind': wind
    }

    weather_data = get_weather(api_key, location)
    if not weather_data:
        return

    alerts = check_conditions(weather_data, thresholds)
    if alerts:
        print("\n*** WEATHER ALERTS ***")
        for alert in alerts:
            print("-", alert)
    else:
        print("No alerts. Weather conditions are within your set thresholds.")

if __name__ == "__main__":
    main()


