from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from lxml import etree
import os
import requests
from utils import get_browser
import glob
import re
import time

def get_page_source(url):
    browser = get_browser(headless=False)
    browser.get(url)
    # Scroll down the page
    wait = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[2]/tm-gallery-view/div/div"))
    )

    height = browser.execute_script("return document.body.scrollHeight")
    browser.execute_script(
        "window.scrollTo(0, " + str(height/3) + ");")
    time.sleep(2)

    try:
        wait = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[3]/tg-row[1]/tg-col[1]/tm-property-listing-body/div/div/section[2]/div/tm-property-homes-pi-banner/div'))
        )

        cv_button = browser.find_element(
            by="xpath", value="/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[3]/tg-row[1]/tg-col[1]/tm-property-listing-body/div/div/section[2]/div/tm-property-homes-pi-banner/div/tg-tabs/tg-scrollable-container/div/div/div/tg-tab[2]/a")
        cv_button.click()

    except TimeoutException:
        print(f"time out to locate the cv_button for property")

    return browser.page_source


def download_imgs(tree, url) -> str:
    thumbnails = tree.xpath(
        "/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[2]/tm-gallery-view/div/div/tm-gallery-thumbnail-slider/div/div/div")

    # https://www.trademe.co.nz/a/property/residential/sale/auckland/auckland-city/mount-roskill/listing/3969505637?rsqid=16ce08b7d4df422e966c890743fd2222-001
    property_id = url.split("/")[-1][:10]
    save_dir = f"/home/walter/git/webCrawler/trademe/images/{property_id}"
    os.makedirs(save_dir, exist_ok=True)

    for thumbnail in thumbnails:
        img_src = thumbnail.xpath("./img/@src")[0]
        img_name = img_src.split("/")[-1]
        # 480m   full   1024sq    plus
        fullsize_img_src = "https://trademe.tmcdn.co.nz/photoserver/1024sq/" + img_name
        response = requests.get(fullsize_img_src)
        if response.status_code == 200:
            save_path = os.path.join(save_dir, img_name)
            if not os.path.exists(save_path):
                with open(save_path, "wb") as f:
                    f.write(response.content)
                    print("download successful for ", img_name)

    all_jpg = glob.glob(f"{save_dir}/*.jpg")

    if len(all_jpg) > 0:
        return all_jpg[0]
    else:
        return save_dir


def get_attributes_dict(tree) -> dict:
    attrs = tree.xpath(
        "/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[3]/tg-row[1]/tg-col[1]/tm-property-listing-body/div/section[1]/tm-property-listing-attributes/section/ul[1]/li")

    attributes_dict = {}
    for attr in attrs:
        # [' \xa0 4 Beds '] [' \xa0 2 Baths '] [' \xa0 1 Living area ']
        raw_text = attr.xpath(
            "./tm-property-listing-attribute-tag/tg-tag/span/div/text()")[0].split()
        text = raw_text
        quantity = text[0]
        feature = " ".join(text[1:])
        attributes_dict[feature] = quantity

    return attributes_dict


def get_address_dict(tree) -> dict:
    # ['106G Gowing Drive, Meadowbank, Auckland City, Auckland']
    address = tree.xpath(
        "/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[3]/tg-row[1]/tg-col[1]/tm-property-listing-body/div/section[1]/h1/text()")[0].split(",")
    address_dict = {}
    if len(address) < 4: 
        return address_dict
    address_dict["street"] = address[0]
    address_dict["suburb"] = address[1]
    address_dict["district"] = address[2]
    address_dict["region"] = address[3]

    return address_dict


def get_cv_dict(tree) -> dict:
    cv_dict = {}

    cv = tree.xpath(
        '/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[3]/tg-row[1]/tg-col[1]/tm-property-listing-body/div/div/section[2]/div/tm-property-homes-pi-banner/div/tg-tabs/div/div/tg-tab-content/tm-property-homes-pi-banner-capital-value/div[1]/p[1]/text()')
    land_value = tree.xpath(
        '/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[3]/tg-row[1]/tg-col[1]/tm-property-listing-body/div/div/section[2]/div/tm-property-homes-pi-banner/div/tg-tabs/div/div/tg-tab-content/tm-property-homes-pi-banner-capital-value/div[2]/p[2]/text()')
    improvement_value = tree.xpath(
        '/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[3]/tg-row[1]/tg-col[1]/tm-property-listing-body/div/div/section[2]/div/tm-property-homes-pi-banner/div/tg-tabs/div/div/tg-tab-content/tm-property-homes-pi-banner-capital-value/div[2]/p[4]/text()')

    cv_dict['cv'] = cv[0] if len(cv) > 0 else None
    cv_dict['land_value'] = land_value[0] if len(land_value) > 0 else None
    cv_dict['improvement_value'] = improvement_value[0] if len(improvement_value) > 0 else None
    

    return cv_dict


def get_sale_method(tree) -> str:
    sale_method = tree.xpath(
        "/html/body/tm-root/div[1]/main/div/tm-property-listing/div/div[3]/tg-row[1]/tg-col[1]/tm-property-listing-body/div/section[1]/h2[2]/strong/text()")[0]

    return sale_method


def is_new_home(url):
    pattern = r"https://www.trademe.co.nz/a/property/(.*?)/"
    match = re.search(pattern, url)
    group = match.group(1)
    return "yes" if "new" in group else "no"


def get_property_detail(url) -> dict:
    page_source = get_page_source(url)
    tree = etree.HTML(page_source)
    
    info_dict = {}
    info_dict["img_dir"] = download_imgs(tree, url)
    info_dict["sale_method"] = get_sale_method(tree)
    info_dict["new_home"] = is_new_home(url)
    info_dict.update(get_attributes_dict(tree))
    info_dict.update(get_address_dict(tree))
    info_dict.update(get_cv_dict(tree))

    return info_dict


