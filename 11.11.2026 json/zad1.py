import json


products = [
    {"name": "Mouse", "price": 75, "stock": 5},
    {"name": "Keyboard", "price": 150, "stock": 3},
    {"name": "Monitor", "price": 800, "stock": 2}
]


def save_products(products):
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)

def load_products():
    
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            result = json.load(file)

            return result
    except FileNotFoundError:
        print("File does not exist")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON")
        return []

#save_products(products)
print(load_products())