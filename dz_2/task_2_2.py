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
        b.append(f'{str_c}{int(str_b):02d}')
        b.append('"')
    else:
        b.append(str_b)
b.reverse()
print(' '.join(b))
