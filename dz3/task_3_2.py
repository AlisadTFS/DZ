def num_translate_adv(en_numb):
    rus_list = {'zero': 'ноль',
                'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'teen': 'десять'}
    if en_numb.istitle:
        print(rus_list.get(en_numb.lower(), 'перевод не найден, ждите обновления словаря').title())
    else:
        print(rus_list.get(en_numb, 'перевод не найден, ждите обновления словаря'))


en_number = input('Введите число на анг: ')
num_translate_adv(en_number)
