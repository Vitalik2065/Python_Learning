products = [
    {"name": "Mouse", "price": 75},
    {"name": "Keyboard", "price": 150},
    {"name": "Monitor", "price": 800}
]



def get_product_value(products, index, key):
    try:
        return products[index][key]
    except IndexError:
        print("We don`t have index like that")
        return None
    except KeyError:
        print("We don`t have key like that/")
        return None



print(get_product_value(products, 0, "name"))
print(get_product_value(products, 1, "price"))
print(get_product_value(products, 10, "name"))
print(get_product_value(products, 0, "stock"))
print(get_product_value(products, -1, "name"))