a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, s in enumerate(a):
    if s.isdigit():
        a[i] = f'"{int(s):02d}"'
    elif s[1:].isdigit():
        a[i] = f'"{s[0]}{int(s[1:]):02d}"'
    print(a[i], end=' ')
