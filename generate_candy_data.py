import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

print("🍬 Baking our Candy Shop data... please wait a few seconds!")

# 1. Setup pretend shop rules
random.seed(42)
np.random.seed(42)

TOTAL_CUSTOMERS = 1000
TOTAL_VISITS = 6000

# Kids' favorite candy types and prices
PRODUCTS = {
    'Choco-Blast Bar': 4.50,
    'Super Gummy Worms': 2.50,
    'Rainbow Lollipop': 1.50,
    'Fizzy Soda Pop': 3.00,
    'Giant Candy Box': 12.00
}

# How the kids heard about the shop
CHANNELS = ['School Poster', 'Friend Told Me', 'YouTube Ad', 'Instagram', 'Walked By']

# 2. Create pretend customers
start_date = datetime(2025, 1, 1)

customers = []
for cid in range(1, TOTAL_CUSTOMERS + 1):
    first_visit = start_date + timedelta(days=random.randint(0, 300))
    first_channel = random.choice(CHANNELS)
    city = random.choice(['Nicosia', 'Larnaca', 'Limassol', 'Paphos', 'Famagusta'])
    
    customers.append({
        'Customer_ID': f"KID_{cid:04d}",
        'First_Visit_Date': first_visit,
        'Signup_Channel': first_channel,
        'City': city
    })

df_customers = pd.DataFrame(customers)

# 3. Create pretend cash register receipts
receipts = []
for rid in range(1, TOTAL_VISITS + 1):
    # Pick a random customer
    cust = df_customers.sample(1).iloc[0]
    
    # Visit happens on or after their first visit
    visit_date = cust['First_Visit_Date'] + timedelta(days=random.randint(0, 60))
    
    product_name = random.choice(list(PRODUCTS.keys()))
    quantity = random.randint(1, 4)
    item_price = PRODUCTS[product_name]
    total_spent = quantity * item_price
    
    receipts.append({
        'Receipt_ID': f"REC_{rid:05d}",
        'Customer_ID': cust['Customer_ID'],
        'Order_Date': visit_date,
        'Product_Name': product_name,
        'Quantity': quantity,
        'Item_Price': item_price,
        'Total_Spent': total_spent,
        'City': cust['City'],
        'First_Channel': cust['Signup_Channel']
    })

df_receipts = pd.DataFrame(receipts)

# Sort them nicely by date
df_receipts = df_receipts.sort_values(by='Order_Date').reset_index(drop=True)

# 4. Save to an Excel/CSV file!
filename = "candy_shop_data.csv"
df_receipts.to_csv(filename, index=False)

print(f"🎉 Success! Created '{filename}' with {len(df_receipts)} receipts!")
print("Here is a peek at the first 3 rows:")
print(df_receipts[['Receipt_ID', 'Customer_ID', 'Order_Date', 'Product_Name', 'Total_Spent']].head(3))