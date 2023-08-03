import requests
import json 


url = "https://fanyi.baidu.com/sug"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

search_word = "dog"
data = {
    "kw": search_word
}

response = requests.post(url=url, data=data, headers=headers)

obj_json = response.json()

fp = open(f"{search_word}.json", "w", encoding="utf-8")
# chinese not support ascii
json.dump(obj=obj_json, fp=fp, ensure_ascii=False)

