import urllib.request
import json


API_KEY = "6dca349e9833448e2a7c82090b1d153b"
city = input("enter city name:")

url = ""
with urllib.request.urlopen(url) as response:

  data = json.loads(response.read().decode())

print("city:", data["name"])
print("temperature:", data["main"]["temp"],"c")
print("weather", data["weather"][0]["description"])