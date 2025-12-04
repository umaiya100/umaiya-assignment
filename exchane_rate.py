
import json
import urllib

API_KEY = "6dca349e9833448e2a7c82090b1d153b"

base_currency = "USD"

target_currency = "TZS"

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"




if data["result"] == "success":
    rate = data["conversion_rates"][target_currency]
    print(f"1 {base_currency} = {rate} {target_currency}")
else:
    print("Error:")