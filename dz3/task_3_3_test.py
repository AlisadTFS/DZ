user_names = ['Иван', 'Петр', 'Ольга', 'Сергей']
user_logins = ['ivan', 'petr', 'olga', 'sergey']
user_roles = ['user', 'staff', 'admin', 'user']

for name, login, role in zip(user_names, user_logins, user_roles):
   print(f'{name}, {login}, {role}')