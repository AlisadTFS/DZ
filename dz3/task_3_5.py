from random import choice


def get_jokes(col):
    list_jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for jokes in range(col):
        list_jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return list_jokes

print(get_jokes(8))
