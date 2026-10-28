import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    arr = np.asarray(values, dtype=float)
    return arr.reshape(-1, width).tolist()


def block(matrix: list[list[float]], rows: list[int],
          columns: list[int]) -> list[list[float]]:
    if not matrix or not rows:
        return []

    arr = np.asarray(matrix, dtype=float)
    return arr[np.ix_(rows, columns)].tolist()
