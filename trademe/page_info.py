from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
from utils import get_url, get_browser
import re


def get_total_page_number(url):

    browser = get_browser(headless=True)
    browser.get(url)

    # Wait for an element to be present on the page
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/tm-root/div[1]/main/div/tm-property-search-component/div/div/tm-property-search-results/div/div[3]/tm-search-results"))
    )

    page_source = browser.page_source
    tree = etree.HTML(page_source)
    last_page_num = tree.xpath(
        "/html/body/tm-root/div[1]/main/div/tm-property-search-component/div/div/tm-property-search-results/div/div[3]/tm-search-results/div/div[2]/tg-pagination/nav/ul/li[10]/tg-pagination-link/a/text()")[0]
    return int(last_page_num.strip())


def get_property_dict_on(page_num, search_conditions):
    url = get_url(page_num=page_num, **search_conditions)
    browser = get_browser(headless=True)
    browser.get(url)

    wait_for_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tm-search-results"))
    )

    page_source = browser.page_source
    tree = etree.HTML(page_source)
    property_list = tree.xpath(
        "/html/body/tm-root/div[1]/main/div/tm-property-search-component/div/div/tm-property-search-results/div/div[3]/tm-search-results/div/div[2]/tg-row/tg-col[@class='l-col l-col--has-flex-contents ng-star-inserted']")

    id_url_dict = {}
    for property in property_list:
        href = property.xpath(".//a/@href")[0]
        href = "/a/" + href if href.startswith("property") else href
        property_id = re.findall("/listing/(\d+)", href)[0]
        property_url = "https://www.trademe.co.nz" + href

        if property_id not in id_url_dict:
            id_url_dict[property_id] = property_url

    return id_url_dict
