from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import json
import requests


def get_photo(city, state):
    url = f"https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": f"{city} {state}", "per_page": 1}
    response = requests.get(url, headers=headers, params=params)
    parsed_json = json.loads(response.content)
    picture_url = parsed_json["photos"][0]["src"]["original"]
    print(picture_url)
    print(json.loads(response.content))
    return {"picture_url": picture_url}
def get_weather(city, state):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},US&appid={OPEN_WEATHER_API_KEY}"
    geocoding_response = requests.get(url)
    geocoding = json.loads(geocoding_response.content)
    geocode = {"lat": geocoding[0]["lat"], "lon": geocoding[0]["lon"]}
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={geocode["lat"]}&lon={geocode["lon"]}&appid={OPEN_WEATHER_API_KEY}&units=imperial'
    )
    res_weather = json.loads(response.content)
    weather = {
        "temp": res_weather["main"]["temp"],
        "description": res_weather["weather"][0]["description"],
    }
    return weather