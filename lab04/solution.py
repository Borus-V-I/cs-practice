def winner(names: list[str], scores: list[float]) -> str:
    if len(scores) == 0:
        return ''
    best_index = 0
    for i in range(1,len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i
    return names[best_index]

def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0
    avg = 0
    for i in scores:
        avg += i
    return round(avg / len(scores),2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices = list(range(len(names)))

    indices.sort(key=lambda i: scores[i], reverse = True)

    res = []

    for i in indices:
        res.append(names[i])
    return res

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = average(scores)
    res = []
    for i in range(len(names)):
        if scores[i] > avg:
            res.append(names[i])
    return res

names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

print(winner(names,scores))
print(average(scores))
print(ranking(names,scores))
print(above_average(names,scores))