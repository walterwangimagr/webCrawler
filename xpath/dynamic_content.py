from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import os
import requests

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

browser.get('https://pic.netbian.com/4kfengjing/')

# Wait for an element to be present on the page
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "slist"))
)

page_source = browser.page_source

with open("xpath/4k.html", "w") as f:
    f.write(page_source)

# Do something with the page source
tree = etree.HTML(page_source)
lis = tree.xpath("/html/body/div[2]/div/div[3]/ul/li")
base_url = "https://pic.netbian.com"
img_dir = "xpath/imgs"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

for li in lis:
    img_src = li.xpath(".//img/@src")[0]
    img_name = img_src.split("/")[-1]
    img_src = base_url + img_src
    print(img_src)
    img_src = "https://pic.netbian.com/uploads/allimg/180826/113958-1535254798fc1c.jpg"
    img_src = "https://pic.netbian.com/uploads/allimg/230124/002504-16744911041d23.jpg"
    img_data = requests.get(url=img_src).content

    save_path = os.path.join(img_dir, img_name)
    print(save_path)
    with open(save_path, 'wb') as f:
        f.write(img_data)
    break

browser.quit()
