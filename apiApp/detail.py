import requests
endpoint="http://127.0.0.1:8080/product/mixin/4/detail"
response=requests.get(endpoint)
print(response.json())
print(response.status_code)