import csv
import re

input_file = "prices.csv"
output_file = "prices_clean.csv"

cleaned_prices = []

# Читаем исходный CSV
with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # пропускаем заголовок
    for row in reader:
        if not row:
            continue
        raw_price = row[0]

        # Убираем "₽/мес." и пробелы, оставляем только цифры
        cleaned = re.sub(r"[^0-9]", "", raw_price)

        if cleaned.isdigit():
            cleaned_prices.append(int(cleaned))

# Записываем результат в новый CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Цена (руб/мес)"])  # заголовок
    for price in cleaned_prices:
        writer.writerow([price])

print(f"Обработанные данные сохранены в {output_file}")