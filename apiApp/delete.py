import requests
id= input("Entrer l'identifiant du produit à supprimer")
endpoint=f"http://127.0.0.1:8080/product/mixin/{id}/delete"
response=requests.delete(endpoint)
# print(response.json())
print(response.status_code)