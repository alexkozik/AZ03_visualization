# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
import re
import pandas as pd

import matplotlib.pyplot as plt

# Настройки для Selenium с Firefox
gecko_driver_path = "/snap/bin/geckodriver"  # Укажите путь к geckodriver
service = Service(gecko_driver_path)
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме (без открытия браузера)

#Если мы работаем с Firefox
driver = webdriver.Firefox(service=service, options=options)

url = "https://www.divan.ru/category/divany-i-kresla?types%5B%5D=1"
driver.get(url)

# Ждём загрузку страницы
time.sleep(3)

# Прокрутка страницы вниз для подгрузки всех товаров
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # ждём подгрузку
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Находим все элементы с ценами
price_elements = driver.find_elements(By.CLASS_NAME, "ui-LD-ZU")  # класс для цен

prices = []
for el in price_elements:
    price_text = el.text.strip()
    # Извлекаем только цифры (убираем "руб." и пробелы)
    match = re.findall(r"\d+", price_text)
    if match:
        price = int("".join(match))
        prices.append(price)

driver.quit()

# Сохраняем цены в CSV
df = pd.DataFrame(prices, columns=["price"])
df.to_csv("divan_price_clean.csv", index=False)

print(f"Собрано {len(prices)} цен. Сохранено в divan_price_clean.csv")

# Загружаем данные
df = pd.read_csv("divan_price_clean.csv")

print('\n'+f"Средняя цена дивана по выборке: {df['price'].mean().round(2)}")

# Строим гистограмму цен
plt.figure(figsize=(10, 6))
plt.hist(df["price"], bins=50, edgecolor='black')
plt.title("Гистограмма цен на диваны")
plt.xlabel("Цена")
plt.ylabel("Частота")
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()