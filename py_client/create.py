import requests

endpoint = ' http://127.0.0.1:8000/api'

data = {
    "title": "MSI",
    "price": 16.90,
    "category": 2
}

response = requests.post(f'{endpoint}/products/', json=data)
# response = requests.get(endpoint)

print("Response status : ", response.status_code)
# print("Response Text : ", response.text)
print("Response JSON : ", response.json())
