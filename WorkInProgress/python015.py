import requests

base = "https://example.com/arquivo{}.txt"

for i in range(1, 4):
    url = base.format(i)
    r = requests.get(url)
    with open(f"arquivo{i}.txt", "wb") as f:
        f.write(r.content)