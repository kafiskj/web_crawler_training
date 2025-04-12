import requests
from bs4 import BeautifulSoup
import csv
import re

url = "http://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#find max page
page_text = soup.select_one("li.current").text.strip()
match = re.search(r'Page \d+ of (\d+)', page_text)
max_page = int(match.group(1)) if match else 1

# 爬全部頁面
book_list = []
for page in range(1, max_page + 1):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select(".product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()
        availability = book.select_one(".availability").text.strip()
        book_list.append({
            "title": title,
            "price": price,
            "availability": availability
        })

# save csv
with open("static.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["title", "price", "availability"])
    writer.writeheader()
    writer.writerows(book_list)

