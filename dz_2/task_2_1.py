def check_class(example):
    if isinstance(example, int):
        return f'{example:>3} - Целое число'
    if isinstance(example, float):
        return f'{example:>3} - Число с плавающей точкой'


a = 15 * 3
print(check_class(a))
a = 15 / 3
print(check_class(a))
a = 15 // 2
print(check_class(a))
a = 15 ** 2
print(check_class(a))
