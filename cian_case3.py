import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_csv("prices_clean.csv")

# Проверим, какие есть столбцы
print(df.head())

# Строим гистограмму цен
plt.figure(figsize=(10, 6))
plt.hist(df["Цена (руб/мес)"], bins=10, edgecolor='black')
plt.title("Гистограмма цен")
plt.xlabel("Цена")
plt.ylabel("Частота")
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()