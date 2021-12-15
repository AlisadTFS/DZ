def check_class(example):
    if isinstance(example, int):
        return f'{example} - Целое число'
    if isinstance(example, float):
        return f'{example} - Число с плавающей точкой'


a = 15 * 3
print('15 * 3 = ', check_class(a))
a = 15 / 3
print('15 / 3 =', check_class(a))
a = 15 // 2
print('15 // 2 =', check_class(a))
a = 15 ** 2
print('15 ** 2 =', check_class(a))
