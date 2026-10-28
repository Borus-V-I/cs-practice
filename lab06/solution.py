def count_items(values: list) -> dict:
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def unique_sorted(values: list) -> list:
    return sorted(set(values))

def common(first: list, second: list) -> list:
    return sorted(set(first) & set(second))

def only_in_first(first: list, second: list) -> list:
    return sorted(set(first) - set(second))

values = ["ошибка", "запуск", "ошибка", "проверка"]

count_items(values)    # {"ошибка": 2, "запуск": 1, "проверка": 1}
unique_sorted(values)  # ["запуск", "ошибка", "проверка"]

common(["иванов", "петрова"], ["петрова", "котов"])        # ["петрова"]
only_in_first(["иванов", "петрова"], ["петрова", "котов"]) # ["иванов"]