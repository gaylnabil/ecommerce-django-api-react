import requests

endpoint = ' http://127.0.0.1:8000/api'

# response = requests.get(endpoint)
data = {
    "title": "DELL inspiron",
    "description": "test",
    "price": 79.20
}
response = requests.get(f'{endpoint}/')
# response = requests.get(endpoint)

print("Response status : ", response.status_code)
# print("Response Text : ", response.text)
print("Response JSON : ", response.json())
