import numpy as np
import matplotlib.pyplot as plt

# 2. Генерируем массив с диапазоном значений от -10 до 10, делаем между ними равное распределение:

x = np.linspace(-10, 10, 100)

# 3. Вычисляем значение данных:

y = x**2

# 4. Создаём график:

plt.plot(x, y)
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.title("График функции y = x**2")

# 5. Делаем сетку на фоне графика:

plt.grid(True)
plt.show()

