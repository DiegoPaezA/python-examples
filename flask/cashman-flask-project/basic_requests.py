import requests
url = "http://127.0.0.1:5000/incomes"
response = requests.get(url=url)
print(response.text)

header = {"Content-Type": "application/json"}
payload = {"amount": 5.0, "description": "test diego 2"}

post_response = requests.post(url=url, json=payload, headers=header)
print("post request done \n")

response = requests.get(url=url)
print(response.text)