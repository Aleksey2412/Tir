import requests
from bs4 import BeautifulSoup

# Устанавливаем User-Agent, чтобы имитировать запрос от обычного браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

# URL страницы с товарами
base_url = "https://www.vamsvet.ru/catalog/section/standart-lamp/"

# Отправляем GET-запрос на сайт с указанием User-Agent
response = requests.get(base_url, headers=headers)

# Проверяем статус-код ответа
if response.status_code != 200:
    raise Exception(f"Request failed with status code {response.status_code}")

# Парсим HTML-документ
soup = BeautifulSoup(response.text, 'html.parser')

# Извлекаем все товары с карточки товаров
products = soup.select(".product-list-item")

for product in products:
    # Название товара
    title = product.select_one(".product-title").text.strip()

    # Цена товара
    price = product.select_one(".price-current").text.strip()

    # Ссылка на товар
    link = product.select_one(".product-link")["href"]

    # Выводим результат
    print(f"Название: {title}\nЦена: {price}\nСсылка: {link}\n")
