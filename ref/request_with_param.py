import requests
import os

url = "https://www.trademe.co.nz/a/property/residential/sale"

region = "auckland"
district = "auckland-city"
price_min = 1000000
price_max = 1800000
bedrooms_min = 4
property_type = "house"
bathrooms_min = 2


url = os.path.join(url, region, district)

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


params = {
    "price_min": price_min,
    "price_max": price_max,
    "bedrooms_min": bedrooms_min,
    "property_type": property_type,
    "bathrooms_min": bathrooms_min,
}

response = requests.get(url=url, params=params, headers=headers)
response_text = response.text
with open(f"{region}_trame.html", "w", encoding="utf-8") as f:
    f.write(response_text)

