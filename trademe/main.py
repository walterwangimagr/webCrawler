from page_info import get_total_page_number, get_property_dict_on
from utils import get_url
import json

def get_id_url_dict():
    id_url_dict = {}
    for page_num in range(1, total_page_num+1):
        print(f"crawling page {page_num}")
        for i in range(10):
            property_id_url_dict = get_property_dict_on(
                page_num, search_conditions)
            if len(property_id_url_dict) > 0:
                print(f"found {len(property_id_url_dict)} properties on page {page_num}")
                break
            print(f"retry page {page_num} for {i+1} time")

        id_url_dict.update(property_id_url_dict)
    return id_url_dict

search_conditions = {
    "price_min": 1000000,
    "price_max": 1800000,
    "bedrooms_min": 4,
    "property_type": "house",
    "bathrooms_min": 2
}

first_page_url = get_url(page_num=1, **search_conditions)
total_page_num = get_total_page_number(first_page_url)

id_url_dict = get_id_url_dict()

with open("result.json", "w") as f:
    json.dump(id_url_dict, f)
