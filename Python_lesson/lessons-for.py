for i in range(1, 5):
    print(i)
else:
    print('Цикл for закончен')

while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    print('Длина строки:', len(s))
print('Завершение')