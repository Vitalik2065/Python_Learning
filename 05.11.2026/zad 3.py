



def validate_price(price):
    if type(price) is int:
    
        if price < 0:
            raise ValueError("Price cannot be negative")

        return price
    else:
        raise TypeError("it has to be integer")

        

    




try:
    result = validate_price("10")

except ValueError:
    print("Error")

except TypeError:
    print("it has to be integer")

else:
    print("Success:", result)

finally:
    print("Finished")