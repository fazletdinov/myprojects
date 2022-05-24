number = 23
running = True

while running:
    guess = int(input("Enter an inrege: "))
    if guess == number:
        print("Поздравляю вы угадали")
        running = False # это осталавливает цикл
    elif guess < number:
        print("Нет, загаданное число немного больше этого")
    else:
        print("Нет, загаданное число немного меньше эого")

else:
    print("Цикл while завершен")

print('Завершение')