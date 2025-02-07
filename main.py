import requests
import time
import sqlite3

connection = sqlite3.connect("crypto_prices.db")
executing = connection.cursor()

# Create table if not exists
connection.execute("""
    CREATE TABLE IF NOT EXISTS crypto (
    
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        value REAL,
        time DATETIME DEFAULT CURRENT_TIMESTAMP
        
    )
""")
connection.commit()
def fetch_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None
def save_price(currency, price):
    if currency == "Ethereum":
        price = round(price)
    executing.execute("INSERT INTO prices (currency, price) VALUES (?, ?)", (currency, price))
    connection.commit()
    print(f"Saved {currency}: ${price}")

while True:
    data = fetch_price()

    if data:
        save_price("Bitcoin", data["bitcoin"]["usd"])
        save_price("Ethereum", data["ethereum"]["usd"])

    time.sleep(600)  # Fetch every 10 minutes