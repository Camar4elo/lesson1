def format_price(price):
    price_1 = float(price)
    final_price = f"Цена: {price_1} руб."
    return final_price

result = format_price('56.24')
print(result)