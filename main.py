import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.joyces.ie/tablets-tech-computing/laptops/"
header = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"}
session = requests.session()

for j in range(1, 10):
    print(f"PAGE = {j}")
    url = f"https://www.joyces.ie/tablets-tech-computing/laptops/?order=sort-stock&p={j}/"

    response = session.get(url, headers=header)
    # 200-300 ок 300-400 перенаправление 400-500 страница не найдена и 500-600 сервер
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        allProduct = soup.find("div", class_="row cms-listing-row js-listing-wrapper")
        # print(allProduct)
        products = allProduct.find_all("div", class_="product-info")
        for i in range(len(products)):
            try:
                title = products[i].find("a", class_="product-name").text.strip()
                price = products[i].find("span", class_="product-price").text.strip()
                print(title, price)
                with open("product.txt", "a", encoding="UTF-8") as file:
                    file.write(f"{title} --->>> {price}\n")
            except:
                print(title, price)
