def num_translate(en_numb):
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
    print(rus_list.get(en_numb))


en_number = input('Введите число на анг: ')
num_translate(en_number)
