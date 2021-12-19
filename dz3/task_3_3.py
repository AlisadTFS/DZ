def thesaurus(*arge):
    name = {}
    for el in arge:
        name[el[0]] = name.get(el[0], []) + [el]
    return name


print(thesaurus("Иван", "Мария", "Петр", "Илья"))