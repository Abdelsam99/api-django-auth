import requests
endpoint="http://127.0.0.1:8080/product/2/update/"
response=requests.put(endpoint, json={"name":"Sam", "price":50, "content":"Moi" })
print(response.json())
print(response.status_code)