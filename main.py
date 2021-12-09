res = ''
duration = int(input('Введите число: '))
day_result = duration // 86400
if day_result > 0:
    res = str(day_result) + ' дн. '
hour_result = (duration - day_result * 86400) // 3600
if hour_result > 0:
    res = res + str(hour_result) + ' час. '
minut_result = (duration - day_result * 86400 - hour_result * 3600) // 60
if minut_result > 0:
    res = res + str(minut_result) + ' мин. '
second_result = duration - day_result * 86400 - hour_result * 3600 - minut_result * 60
if second_result > 0:
    res = res + str(second_result) + ' сек. '
print(res)