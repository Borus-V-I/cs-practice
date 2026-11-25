import numpy as np


# 1. Создание таблицы
def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()


# 2. Получение прямоугольного фрагмента матрицы
def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.array(matrix)

    return arr[row_start:row_stop, column_start:column_stop].tolist()
