from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from lxml import etree
import os
import requests
import glob

def get_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument(
        # "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
    options.add_argument('--headless')
    # options.add_argument("--header=Accept-Language: en-GB,en-US;q=0.9,en;q=0.8")
    browser = webdriver.Chrome(options=options)
    return browser


def get_tree(url):
    browser = get_browser()
    browser.get(url)
    # wait util load js
    element = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='overview']/div[1]/div[1]/div[4]/span"))
    )
    page_source = browser.page_source
    tree = etree.HTML(page_source)
    return tree


url = "https://relab.co.nz/auckland/mount-roskill/20b-morrie-laing-avenue"
tree = get_tree(url)
title_and_land = tree.xpath("//*[@id='overview']/div[1]/div[1]/div[4]/span/text()")[0]
cv = tree.xpath("//*[@id='collapse1057']/div/div[1]/div[2]/div/div[2]/div/span[1]/text()")[0]
land_value = tree.xpath("//*[@id='overview']/div[1]/div[1]/div[4]/span/text()")[0]
house_value = tree.xpath("//*[@id='collapse1057']/div/div[1]/div[3]/div/div[2]/div/span[1]/text()")[0]
floor = tree.xpath("//*[@id='pricebasicinfo']/div/div[1]/div/div[2]/text()")[0]
floor = tree.xpath("//*[@id=‘house_title_gov’]/div[2]/div[6]/div/div[2]/h4/text()")[0]

print(title_and_land)
print(cv)
print(land_value)
print(house_value)
print(floor)