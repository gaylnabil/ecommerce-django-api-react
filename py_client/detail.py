import requests

endpoint = ' http://127.0.0.1:8000/api'

# data = {
#     "title": "DELL inspiron",
#     "description": "test",
#     "price": 79.20
# }
id = 2
headers = {'authorization': 'Bearer 2ab66083fdfe7c9c950bf588ab1e1df21d2256ba'}

response = requests.get(f'{endpoint}/products/{id}/', headers=headers)
# response = requests.get(endpoint)

print("Response status : ", response.status_code)
# print("Response Text : ", response.text)
print("Response JSON : ", response.json())
