
from collections import Counter

# Read the orders
orders = []
try:
    with open('03_feladat.txt', 'r') as f:
        for line in f:
            product, quantity_str = line.strip().split(';')
            orders.append({'product': product, 'quantity': int(quantity_str)})
except FileNotFoundError:
    print("Error: 03_feladat.txt not found.")
    exit()

# Calculate total number of items ordered
total_items = sum(order['quantity'] for order in orders)

# Count "Pékáru" orders
pekáru_orders = sum(order['quantity'] for order in orders if order['product'] == 'Pékáru')

# Filter orders with more than 3 items
orders_over_3 = [order for order in orders if order['quantity'] > 3]

# Find the most ordered product type
product_counts = Counter(order['product'] for order in orders)
most_ordered_product = product_counts.most_common(1)[0][0] if product_counts else None

# Write results to a new file
with open('03_eredmeny.txt', 'w') as f:
    f.write(f"Total items ordered: {total_items}\n")
    f.write(f"Number of 'Pékáru' orders: {pekáru_orders}\n")
    f.write("Orders with more than 3 items:\n")
    for order in orders_over_3:
        f.write(f"- {order['product']};{order['quantity']}\n")
    if most_ordered_product:
        f.write(f"Most ordered product type: {most_ordered_product}\n")

print("Results written to 03_eredmeny.txt")