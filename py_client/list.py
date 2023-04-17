import requests

endpoint = 'http://0.0.0.0:8000/api'  # 'http://127.0.0.1:8000/api'


response = requests.get(f'{endpoint}/products/')
# response = requests.get(endpoint)

print("Response status : ", response.status_code)
# print("Response Text : ", response.text)
print("Response JSON : ", response.json())
