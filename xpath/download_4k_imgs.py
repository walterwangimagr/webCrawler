from selenium import webdriver
from lxml import html

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=options)
browser.get('https://pic.netbian.com/4kfengjing/')

page_source = browser.page_source
with open("xpath/4k.html", "w") as f:
    f.write(page_source)

tree = html.fromstring(page_source)

data = tree.xpath('/html/body')
print(data)

browser.quit()
