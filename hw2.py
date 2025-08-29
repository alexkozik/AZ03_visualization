# 2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)  # массив из 100 случайных чисел
y = np.random.rand(100)  # массив из 100 случайных чисел

plt.scatter(x, y)
plt.title("Диаграмма рассеяния 2 наборов случайных чисел")
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.show()


