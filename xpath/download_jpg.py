import requests

url = "https://pic.netbian.com/uploads/allimg/230124/002504-16744911041d23.jpg"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Cache-Control": 'max-age=0',
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": "Linux",
    "Upgrade-Insecure-Requests": "1",
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' ,
    "Sec-Fetch-Site": 'none',
    "Sec-Fetch-Mode": 'navigate',
    "Sec-Fetch-User": '?1',
    "Sec-Fetch-Dest": 'document',
    "Accept-Encoding": 'gzip, deflate, br',
    "Accept-Language": 'en-GB,en-US;q=0.9,en;q=0.8',
    "cookie": "__yjs_duid=1_9618ae6d85442f944b0faa678f9e91ea1675680940642; Hm_lvt_c59f2e992a863c2744e1ba985abaea6c=1675680946; zkhanecookieclassrecord=%2C53%2C; yjs_js_security_passport=5ad484456ae67e498e9161b04728d29b49639d92_1675716529_js; Hm_lpvt_c59f2e992a863c2744e1ba985abaea6c=1675717622"
}
response = requests.get(url=url, headers=headers)

print(response.status_code)

if response.status_code == 200:
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
