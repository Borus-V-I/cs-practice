names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

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

