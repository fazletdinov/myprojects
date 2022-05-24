import requests
from api_token import API_TOKEN
params = {"q": "Уфа", "appid": API_TOKEN, "units": "metric"}
response = requests.get("https://api.openweathermap.org/data/2.5/weather/", params=params)

print(response.text)