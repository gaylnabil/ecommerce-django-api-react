import requests

endpoint = ' http://127.0.0.1:8000/api'

data = {
    "title": "Dell Precision m3800",
    "description": "Dell Precision m3800 (Windows 11, 16GB RAM, 1T HDD, Intel Core i7 Gen 11th, Silver, 14.0 Inch)",
    "price": 12999.00
}
# data = {
#     "title": "MSI Prestige PS63 8SC",
#     "description": "RAM: 16 GB CPU: i7-8565U Display Size: 15.6 inch Storage Size: 512 GB Graphics Card: NVIDIA GeForce GTX 1650, NVIDIA GeForce GTX 1650 Max-Q",
#     "price": 26990.00
# }
id = 6
response = requests.put(f'{endpoint}/products/{id}/update/', json=data)
# response = requests.get(endpoint)

print("Response status : ", response.status_code)
# print("Response Text : ", response.text)
print("Response JSON : ", response.json())
