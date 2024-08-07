# Calculates the gross price of products in Wonderland.

def calculate_gross_price(net_price):
    gross_price = net_price + (0.08 * net_price)
    return gross_price
