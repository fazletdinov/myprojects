class C1:
    def meth1(self): self.__x = 88
    def meth2(self): print(self.__x)

class C2:
    def metha(self): self.__x = 99
    def methb(self): print(self.__x)

class C3(C1, C2): pass

i = C3()
print(i.meth1(), i.metha())
print(i.__dict__)
print(i.methb(), i.meth2())
