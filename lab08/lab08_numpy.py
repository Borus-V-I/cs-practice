import numpy as np


# Задание 1. Создание векторов и матриц

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:")
print(unknown_table)
print("identity:")
print(identity)


# Задание 2. Индексы и срезы вектора

print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Индексы 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


# Задание 3. Строки и столбцы таблицы

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\nЗадание 3")
print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])
print("Центральный фрагмент 2x2:")
print(temperatures[:2, 1:3])
print("Форма центрального фрагмента:", temperatures[:2, 1:3].shape)


# Задание 4. Прямоугольные срезы

matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
print("Матрица:")
print(matrix)

first_three = matrix[:3, :]
print("Первые три строки:")
print(first_three)
print("shape:", first_three.shape)

last_two = matrix[-2:, :]
print("Последние две строки:")
print(last_two)
print("shape:", last_two.shape)

first_two_columns = matrix[:, :2]
print("Первые два столбца:")
print(first_two_columns)
print("shape:", first_two_columns.shape)

fragment = matrix[1:4, 2:5]
print("Фрагмент строк 1–3 и столбцов 2–4:")
print(fragment)
print("shape:", fragment.shape)

corner = matrix[-2:, -2:]
print("Правый нижний блок 2x2:")
print(corner)
print("shape:", corner.shape)
