# a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# for s in a:
#     for symbol in s:
#         if symbol in ['+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#             print(s)
# message = 'мривет всем'
# print(message[:message.index(' ')])
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
name, year, month, money = 'Борис', 2021, 3, 1789.47689
# mes = '{2}! Сегодня {1} месяц {0} года.'.format(year, month, name)
# mes_2 = '{2:^15}! Сегодня {1:02d} месяц {0} год.'.format(year, month, name)
# mes_3 = f'{name:<15}! На счете {money:.2f}'.format(name=name, money=money)
# print(mes)
# print(mes_2)
# print(mes_3)
mes = f'Уважаемый, {name}! Поздравляем с {year} годом!'
print(mes)