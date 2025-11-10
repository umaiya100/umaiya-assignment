

import re

url = "https://example.com/news/2025/11/10/article"

match = re.search(r'(\d{4})[/-](\d{1,2})[/-](\d{1,2})', url)

if match:
    year, month, day = match.groups()
    print("Year:", year)
    print("Month:", month)
    print("Day:", day)
else:
    print("No date found in URL")