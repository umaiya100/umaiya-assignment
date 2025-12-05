import urllib.request
import json


language = input("enter a language:")

word = input("whats the word?")

URL = f"https://freedictionaryapi.com/api/v1/entries/{language}/{word}"

with urllib.request.urlopen(URL) as response:
    parsed_data = json.loads(response.read().decode())
    senses = parsed_data["entries"][0]["senses"]

    for sense in senses:
        print(sense["definition"])
        print()