# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и
# дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут',
# 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как
# модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его
# реализации позже. Главное: дополнить числа до двух разрядов нулём!

a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
b = []
# str_b = ''
# str_c = ''
while len(a) > 0:
    str_a = a.pop()
    if str_a[0] in ('+', '-'):
        str_b = str_a[1:]
        str_c = str_a[:1]
    else:
        str_b = str_a
        str_c = ''
    if str_b.isdigit():
        b.append('"')
        if int(str_b) < 10:
            b.append(f'{str_c}{int(str_b):02d}')
        else:
            b.append(str_b)
        b.append('"')
    else:
        b.append(str_b)
b.reverse()

print(' '.join(b))

# str_a = ','.join(a)
# print(str_a)
# i = 2
# for s in a:
#     for symbol in s:
#         if symbol[0] in ['+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             if int(s) < 10:
#                 a[a.index(s)] = f'0{int(s)}'
#         else:
#             break
#             # print(a.index(s))
# #             a.insert(a.index(s), '"')
# #             a.insert(a.index(s) + i, '"')
# #             i += 2
# print(a)
# message = 'мривет всем'
# print(message[:message.index(' ')])
# print(a[:a.index('+')])
# print(ord(message[0]))
# print(chr(ord(message[0]) - 32))
# print(message[::-1])
# start = ord('A')
# stop = ord('Z')
# message = ''
# while start <= stop:
#     message += chr(start)
#     message += chr(start + 32)
#     start += 1
# print(message)
# for i in range(ord('A'), ord('Z') + 1):
#     message += chr(i)
#     message += chr(i + 32)
# print(message)
# name, year, month, money = 'Борис', 2021, 3, 1789.47689
# mes = '{2}! Сегодня {1} месяц {0} года.'.format(year, month, name)
# mes_2 = '{2:^15}! Сегодня {1:02d} месяц {0} год.'.format(year, month, name)
# mes_3 = f'{name:<15}! На счете {money:.2f}'.format(name=name, money=money)
# print(mes)
# print(mes_2)
# print(mes_3)
# mes = f'Уважаемый, {name}! Поздравляем с {year} годом!'
# print(mes)
