import requests

endpoint = ' http://127.0.0.1:8000/api'

# data = {
#     "title": "DELL inspiron",
#     "description": "test",
#     "price": 79.20
# }
id = 2
response = requests.get(f'{endpoint}/products/{id}/')
# response = requests.get(endpoint)

print("Response status : ", response.status_code)
# print("Response Text : ", response.text)
print("Response JSON : ", response.json())
