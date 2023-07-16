import requests

endpoint = ' http://127.0.0.1:8000/api'

# data = {
#     "title": "DELL inspiron",
#     "description": "test",
#     "price": 79.20
# }
id = 2
headers = {'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg5NTM0NDIzLCJpYXQiOjE2ODk1MzQzODMsImp0aSI6IjAzNTRlMjI5NmNiMjQ3NWVhNzY2M2RjYjFiMDViNjMwIiwidXNlcl9pZCI6MX0.Ir1bQEzaws3u0QreGlqeNqsA2DSCp5wv0qcydKRqCmU '}

response = requests.get(f'{endpoint}/products/{id}/', headers=headers)
# response = requests.get(endpoint)

print("Response status : ", response.status_code)
# print("Response Text : ", response.text)
print("Response JSON : ", response.json())
