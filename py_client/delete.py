import requests


product_id = input('What does the Product you want to delete?\n')
try:
    product_id = int(product_id)
except Exception:
    print(f'Error: {product_id} is invalid ID')
    product_id = None

if product_id:
    endpoint = ' http://127.0.0.1:8000/api'
    response = requests.delete(f'{endpoint}/products/{product_id}/delete/')

    print("Response status : ", response.status_code,
          '==>', response.status_code == 204)
