import requests
from getpass import getpass

endpoint = 'http://0.0.0.0:8000/api'  # 'http://127.0.0.1:8000/api'

username = input('Enter your Username: ')
password = getpass('Enter your password: ')
print('password:', password)
auth_response = requests.post(
    f'{endpoint}/auth/', json={'username': username, 'password': password})


print("auth_response status : ", auth_response.status_code)
print("auth_response JSON : ", auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    print("AuthToken : ", token)

    # headers = {'Authorization': f'Token {token}'}
    # Change keyword name from 'Token' to 'Bearer' => CHeck api.authentication
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{endpoint}/products/', headers=headers)
    # response = requests.get(endpoint)

    # print("Response Text : ", response.text)
    print("Response status : ", response.status_code)
    print("Response JSON : ", response.json())
