import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# # Запускаем браузер
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-blink-features=AutomationControlled")
# driver = webdriver.Chrome(options=options)

# Настройки для Selenium с Firefox
gecko_driver_path = "/snap/bin/geckodriver"  # Укажите путь к geckodriver
service = Service(gecko_driver_path)
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме (без открытия браузера)

#Если мы работаем с Firefox
driver = webdriver.Firefox(service=service, options=options)

try:
    url = "https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/"
    driver.get(url)

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@data-mark='MainPrice']")))

    # Собираем цены
    prices_elements = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']")
    prices = [el.text for el in prices_elements]

    # Скроллим вниз для подгрузки новых объявлений
    for i in range(2):  # можно увеличить для большего количества данных
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']")
        for el in new_prices:
            price = el.text
            if price not in prices:
                prices.append(price)

    print("Всего найдено цен:", len(prices))

    # Сохраняем в CSV
    with open("prices.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Цена"])  # заголовок
        for p in prices:
            writer.writerow([p])

    print("Результат сохранён в prices.csv")

finally:
    driver.quit()