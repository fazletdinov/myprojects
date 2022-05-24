# Урок №2

name = "mr IDEl fazletdinov"

print(name.title()) # позволяет сделать первые буквы заглавными
print(name.upper()) # все буквы переводит в верхний регистр
print(name.lower()) # все буквы переводит в нижний регистр

print("Privet stroka nomer 1 \nPrivet stroka nomer 2 \n\nPrivet stroka nomer 3") # начинает с новой строки
print("Message: \n\tMessage1 \n\tMessage2 \n\tMessage3 \n\tMessage4 \nEND")
print("Lower name: " + name.lower())
print("___________________________________\n\n")
a = "     ,,,    ,, vasia  ,,,,         "
print(a)
print(a.rstrip()) # убирает пробелы справа
print(a.lstrip()) # убирает пробелы слева
print(a.strip()) # убирает пробелы с двух сторон
print(a.strip(" " + ",")) # убирает лишние робелы и запятые с обоих сторон