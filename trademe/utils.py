import urllib.parse
from selenium import webdriver


def get_url(page_num,
            price_min, 
            price_max, 
            bedrooms_min, 
            bathrooms_min,
            property_type="house",
            district="auckland-city", 
            region="auckland"): 
    
    base_url = f"https://www.trademe.co.nz/a/property/residential/sale/{region}/{district}/search?"
    params = {
        "price_min": price_min,
        "price_max": price_max,
        "bedrooms_min": bedrooms_min,
        "property_type": property_type,
        "bathrooms_min": bathrooms_min,
        "page": page_num
    }
    encoded_params = urllib.parse.urlencode(params)
    url = base_url + encoded_params

    return url


def get_browser(headless:bool):
    options = webdriver.ChromeOptions()
    options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
    if headless:
        options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    
    return browser


def write_md(results, filename="/home/walter/git/webCrawler/trademe/search_result.md"):
    
        
    with open(filename, 'w') as f:
        f.write('| Images  | Address | Beds | Baths | Floor | Land | sale | cv | land value | increment_value |\n')
        f.write('| ------- | ---- | ---- | ----- | ---- -| ---- | ---- | ---- | ---- | ---- |\n')
        for info_dict in results:
            f.write(f"| [![img]({info_dict['img_dir']})]({info_dict['img_dir']}) | {info_dict['address_dict'].get('street')} ,{info_dict['address_dict'].get('suburb')} | {info_dict['attributes_dict'].get('Beds')} | {info_dict['attributes_dict'].get('Baths')} | {info_dict['attributes_dict'].get('Floor')} | {info_dict['attributes_dict'].get('Land')} | {info_dict['sale_method']} | {info_dict.get('cv_dict').get('cv')} | {info_dict.get('cv_dict').get('land_value')} | {info_dict.get('cv_dict').get('improvement_value')} |\n")


# info = {'img_dir': '/home/walter/git/webCrawler/trademe/images/3944369305/1900328816.jpg', 'attributes_dict': {'Beds': '4', 'Baths': '2', 'Living area': '1', 'Land': '140m²'}, 'address_dict': {'street': '153A Penrose Road', 'suburb': ' Mount Wellington', 'district': ' Auckland City', 'region': ' Auckland'}, 'sale_method': 'Price by negotiation'}
# write_md(info)