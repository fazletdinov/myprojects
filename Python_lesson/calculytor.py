print("Слово stop выведет с калькулятора")

while True:
    s = input("Знак (+, -, *, /): ")
    if s == "stop":
        break
    if s in ("+", "-", "*", "/"):
        x = float(input("x="))
        y = float(input("y="))
        if s == "+":
            print("%.2f" % (x+y))
        elif s == "-":
            print("%.2f" % (x-y))
        elif s == "*":
            print("%.2f" % (x*y))
        elif s == "/":
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль")
    else:
        print("Неверный знак операции")

print("Выход с калькулятора")