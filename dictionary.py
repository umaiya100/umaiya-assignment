import urllib.request
import json



word = input("Please enter a word: ")

URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

def get_info(word):
    with urllib.request.urlopen(URL) as response:
        data = json.loads(response.read().decode())

    entry = data[0]

    print("WORD:", entry["word"])
    print("PART OF SPEECH:", entry["meanings"][0]["partOfSpeech"])
    print("DEFINITION:", entry["meanings"][0]["definitions"][0]["definition"])

get_info(word)






