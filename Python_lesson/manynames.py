x = 11

def f():
    print(x)

def g():
    x = 22
    print(x)

class C:
    x = 33
    def method(self):
        x = 44
        self.x = 55

if __name__ == "__main__":
    print(x)
    f()
    g()
    print(x)

    y = C()
    print(y.x)
    y.method()
    print(y.x)
    print(C.x)

    print(C.method.x)
    print(g.x)