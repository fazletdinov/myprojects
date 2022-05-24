class Name:
    "name descriptor doc"
    def __get__(self, instance, owner):
        print("Извлечь...")
        return instance._name
    def __set__(self, instance, value):
        print("менять...")
        instance._name = value
    def __delete__(self, instance):
        print("удалить...")
        del instance._name

class Person:
    def __init__(self, name):
        self._name = name
    name = Name()

bob = Person("Bob Smith")
print(bob.name)
bob.name = "Robert Smith"
print(bob.name)
del bob.name
print("-"*20)
sue = Person("Sue Jones")
print(sue.name)
print(Name.__doc__)