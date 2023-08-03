import requests
from lxml import etree


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

url = "https://bj.58.com/ershoufang/"


page_text = requests.get(url=url, headers=headers).text

with open("./second_hand_house.html" ,"w") as f:
    f.write(page_text)
# tree = etree.parse("./trademe.html")
tree = etree.HTML(page_text)

# use xpath to find elements
# //element[@attribute='value'] will select all elements
# //element[@attribute='value']/text()[0]

# property location div[@class='property']
# sequential location div[1] means the first div, index start from 1
# xpath ./h3 direct child of the parent element 
# xpath .//h3 any child 
divs = tree.xpath("/html/body/div[1]/div/div/section/section[3]/section[1]/section[2]/div[@class='property']")
for div in divs:
    title = div.xpath(".//h3/@title")
    print(title)
    