celling_result = int(input()) # Порог в цельсиях
n = int(input()) # количество повторений
error_count = 0
exceeding_count = 0
mx_temperature  = float("-inf")
sr = 0
for _ in range(n):
    temp = input().strip() # Ввод температуры
    if temp == "error":
        error_count += 1 #Счетчик ошибок
        continue
    value = float(temp)
    if value > celling_result:
        exceeding_count += 1 # Счетчик превышений пороговой температуры
    if  value > mx_temperature: 
        mx_temperature = value # Нахождение  максимума
    sr = sr + value # Нахождение суммы температур
sr_temperature = sr / (n-error_count) # Вычисление средней температуры

print(n)
print(error_count)
print(exceeding_count)
print(mx_temperature)
print(f"{sr_temperature:.1f}")