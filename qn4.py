import requests

url = "https://dev.beepbeep.tech/v1/sample_customer"

r = requests.get(url)

data = r.json()

data['promotions'] = sorted(data['promotions'], key=lambda k: k['title'])

print(data)
