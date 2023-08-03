from utils import get_browser
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
from selenium import webdriver
import time
import json 

url = "https://www.countdown.co.nz/lists/saved/5284824"


options = webdriver.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
browser = webdriver.Chrome(options=options)

browser.get(url)

time.sleep(60)

cookie = browser.get_cookies()
f1 = open('cookie.txt', 'w')
f1.write(json.dumps(cookie))
f1.close()

browser.close()