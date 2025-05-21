import requests


url = "https://fakestoreapi.com/products"

response = requests.get(url)

if response.status_code == 200:
    products = response.json()
    for product in products:
        print(f"{product['id']} - {product['title']} (${product['price']})")
else:
    print("Failed to fetch products:", response.status_code)
