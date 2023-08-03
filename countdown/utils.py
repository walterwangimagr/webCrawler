from selenium import webdriver



def get_browser(headless:bool):
    options = webdriver.ChromeOptions()
    options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
    if headless:
        options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    
    return browser


