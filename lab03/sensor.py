celling_result = int(input()) # Порог в цельсиях
n = int(input()) # количество повторений
error_count = 0
exceeding_count = 0
mx_temperature  = 0
sr = 0
mx = 0
for i in range(n):
    temp = input().strip() # Ввод температуры
    if temp == "error":
        error_count += 1
        continue
    value = float(temp)
    if value > celling_result:
        exceeding_count += 1
    if  value > mx: 
        mx = value
    sr = sr + value
sr_temperature = sr / (n-error_count)

print(n)
print(error_count)
print(exceeding_count)
print(mx)
print(sr_temperature)