x = 50
def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)

func(x)
print('x по-прежнему', x)
print("=======================================")
x = 100
def func():
    global x
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)

func()
print('Значение x составляет', x)

print("===========================================")

def func_outer():
    x = 2
    print('x равно', x)
    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)
func_outer()
print(x)