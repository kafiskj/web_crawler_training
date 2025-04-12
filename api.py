#This python is get "Bitcoin","Eereumth","Dogecoin" 's price
#Through API
import requests
import csv

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,dogecoin"
}
response = requests.get(url, params=params)
data = response.json()

coins = []
for coin in data:
    coins.append({
        "name": coin["name"],
        "symbol": coin["symbol"],
        "price": coin["current_price"]
    })

with open("api.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "symbol", "price"])
    writer.writeheader()
    writer.writerows(coins)
