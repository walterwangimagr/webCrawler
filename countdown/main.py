from utils import get_browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time
import json 
from lxml import etree


url = "https://www.countdown.co.nz/lists/saved/5284824"

options = webdriver.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
browser = webdriver.Chrome(options=options)

browser.get(url)
wait = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/registration-root/section/div/div/registration-enter-email/section/form/div[1]/fieldset/form-input/input'))
        )

email = browser.find_element(by="xpath", value="/html/body/registration-root/section/div/div/registration-enter-email/section/form/div[1]/fieldset/form-input/input").send_keys("accounts@imagr.co")
continue_button = browser.find_element(by="xpath", value="/html/body/registration-root/section/div/div/registration-enter-email/section/form/div[2]/button")
continue_button.click()

wait = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/registration-root/section/div/div/registration-enter-password/section/form/div[1]/fieldset/form-password-input/form-input-with-icon-button/div/input"))
        )

password = browser.find_element(by="xpath", value="/html/body/registration-root/section/div/div/registration-enter-password/section/form/div[1]/fieldset/form-password-input/form-input-with-icon-button/div/input").send_keys("imagrcountdown123")
continue_button = browser.find_element(by="xpath", value="/html/body/registration-root/section/div/div/registration-enter-password/section/form/div[2]/button")
continue_button.click()

wait = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/wnz-content/div/wnz-saved-lists/div/main/product-grid/cdx-card[1]"))
        )

height = browser.execute_script("return document.body.scrollHeight")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(4)

height = browser.execute_script("return document.body.scrollHeight")
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(80)


page_source = browser.page_source
tree = etree.HTML(page_source)

cards = tree.xpath("/html/body/wnz-content/div/wnz-saved-lists/div/main/product-grid/cdx-card")
print(cards)
print(len(cards))
"/html/body/wnz-content/div/wnz-saved-lists/div/main/product-grid/cdx-card[876]/product-stamp-grid/a/div[1]/figure/picture/img"
id_description_dict = {}
for card in cards:
    #/html/body/wnz-content/div/wnz-saved-lists/div/main/product-grid/cdx-card[1]/product-stamp-grid/a/div[1]/figure/picture/img
    # img_src = card.xpath("./product-stamp-grid/a/div[1]/figure/picture/img/@src")
    # print(img_src)
    description = str(card.xpath("./product-stamp-grid/a/h3/text()")[0]).strip()
    desp_2 = card.xpath("./product-stamp-grid/a/div[2]/product-price-meta/p//@aria-label")
    if desp_2:
        desp_2 = str(desp_2[0]).strip()
    else:
        desp_2 = None
    price = card.xpath("./product-stamp-grid/a/div[2]/product-price/h3/@aria-label")
    if price:
        price = str(price[0]).strip()
    else:
        price = None
    print(desp_2)
    print(price)
    id = str(card.xpath("./product-stamp-grid/a/h3/@id")[0]).split("-")[1]

    id_description_dict[id] = [description, desp_2, price]

f =  open("id_descript.txt", 'w')
f.write(json.dumps(id_description_dict))
time.sleep(1000)