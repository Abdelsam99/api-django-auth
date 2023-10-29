
import requests
from getpass import getpass
endpoint="http://127.0.0.1:8080/api/auth/"
username=input('userName\n')
password=getpass('password\n')
auth_response= requests.post(endpoint, json={'username':username, 'password': password})
print(auth_response.json())

if auth_response.status_code==200:
    endpoint="http://127.0.0.1:8080/product/create/"
    headers={
        'Authorization':'Token a871f51bb4e0b28208d38426074d1db46180e43a'
    }
    response=requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)