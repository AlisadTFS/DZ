# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
from math import floor


def format_list(numb):
    if numb > 1:
        k = numb - floor(numb)
    else:
        k = numb
    k = int(round(k, 2) * 100)
    return k


list_price = [8.15, 98.9, 999.9, 888.8, 54.8, 456, 16, 86.45, 100.57, 1.09, ]
for price in list_price:
    if int(price) < 10:
        str_price = f'0{int(price)}'
    else:
        str_price = f'{int(price)}'
    if format_list(price) < 10:
        str_k = f'0{format_list(price)}'
    else:
        str_k = f'{format_list(price)}'
    print(f'{str_price} руб {str_k} коп.', end=',')

print()

print(list_price, id(list_price))
list_price.sort()
print(list_price, id(list_price))

list_price_lower = sorted(list_price, reverse=True)
print(list_price_lower, id(list_price_lower))

print(sorted(list_price, reverse=True)[:5])