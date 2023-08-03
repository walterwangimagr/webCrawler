import requests

url = "https://www.trademe.co.nz/a/?gclid=Cj0KCQiAz9ieBhCIARIsACB0oGKneFqUUIf8H8S-Av4APSjEMdVJem89znr-EJaPDqHehpZi8DsTZuoaAhgYEALw_wcB&gclsrc=aw.ds"
response = requests.get(url=url)
text = response.text
with open("./trademe.html", "w", encoding="utf-8") as f:
    f.write(text)

    