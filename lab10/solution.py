import numpy as np


# 1. Создание таблицы
def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()


# 2. Получение прямоугольного фрагмента матрицы
def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.array(matrix)

    return arr[row_start:row_stop, column_start:column_stop].tolist()


# 3. Замена прямоугольного фрагмента матрицы
def replace_rectangle(matrix, row_start, row_stop,
                      column_start, column_stop, value):
    arr = np.asarray(matrix)

    result = np.asarray(
        matrix,
        dtype=np.result_type(arr.dtype, np.asarray(value).dtype)
    ).copy()

    result[row_start:row_stop, column_start:column_stop] = value

    return result.tolist()