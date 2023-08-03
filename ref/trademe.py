import requests
from lxml import etree
import json
import pprint

url = "https://www.trademe.co.nz/a/property/residential/sale/auckland/auckland-city/"
url = "https://api.trademe.co.nz/v1/advertising/categorytargetedad/3399.json?price_min=1000000&price_max=1800000&bedrooms_min=4&bathrooms_min=2&property_type=house&region=1&district=7"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

region = "auckland"
district = "auckland-city"
price_min = 1000000
price_max = 1800000
bedrooms_min = 4
property_type = "house"
bathrooms_min = 2


params = {
    "price_min": price_min,
    "price_max": price_max,
    "bedrooms_min": bedrooms_min,
    "property_type": property_type,
    "bathrooms_min": bathrooms_min,
}

response = requests.get(url=url, headers=headers)
response_text = response.json()
pprint.pprint(response_text)
# tree = etree.HTML(response_text)

# property = tree.xpath(
#     "/html/body/tm-root/div[1]/main/div/tm-property-search-component/div/div/tm-property-search-results/div/div[3]/tm-search-results/div/div[2]/tg-row/tg-col[3]/tm-search-card-switcher/tm-property-premium-listing-card/div/a/@href")
# print(property)


# with open(f"{district}_trame.html", "w", encoding="utf-8") as f:
#     f.write(response_text)
