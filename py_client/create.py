import requests

endpoint = ' http://127.0.0.1:8000/api'

data = {
    "title": "MSI",
    "price": 16.90,
    "category": 2
}
headers = {'authorization': 'Bearer fb9e8a9785d8b808e22f33ffda6d0a97f610737e'}

response = requests.post(f'{endpoint}/products/', json=data, headers=headers)
# response = requests.get(endpoint)

print("Response status : ", response.status_code)
# print("Response Text : ", response.text)
print("Response JSON : ", response.json())
