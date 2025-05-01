import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("❌ Could not fetch weather data. Please check the city name or your API key.")

if __name__ == "__main__":
    api_key = "72247c696d739ffcd42989926b6fa4de" 
    city = input("Enter a city name: ")
    get_weather(city, api_key)
