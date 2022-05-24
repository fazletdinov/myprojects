def func(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, "has factor", x)
            break
        x = x - 1
    else:
        print(y, "is prime")
    return x

print(func(13))
print(func(15))
print(func(10))