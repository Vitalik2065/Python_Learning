import json
from pathlib import Path


products = [
    {"name": "Mouse", "price": 75},
    {"name": "Keyboard", "price": 150}
]

def products_to_json(products):
    return json.dumps(products)


def products_from_json(products_json):
    try:
        return json.loads(products_json)
    except json.JSONDecodeError:
        print("Your json string is incorrect")
        return None



products_new = products_to_json(products)
print(products_new)
products_new_2 = products_from_json(products_new)
print(products_new_2)

folder = Path("data")

folder.mkdir(exist_ok=True)
file_path = folder / "products.json"

with open(file_path, "w", encoding="utf-8") as file:
    
    json.dump(products, file, indent=4)

print(file_path.exists())