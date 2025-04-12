import requests
import csv
from datetime import datetime

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

# 抓取時間
fetch_time = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

coins.append({})
coins.append({"name": f"Data fetched at: {fetch_time}", "symbol": "", "price": ""})

with open("api.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "symbol", "price"])
    writer.writeheader()
    writer.writerows(coins)
