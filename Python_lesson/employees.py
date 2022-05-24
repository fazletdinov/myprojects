class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "Does stuff")
    def __repr__(self):
        return f"Empoyee: name={self.name}, salary={self.salary}"

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, "makes food")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer")

class Pizzarobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "makes pizza")

if __name__ == '__main__':
    bob = Pizzarobot("Bob")
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob), print()

    for klass in Employee, Chef, Server, Pizzarobot:
        obj = klass(klass.__name__)
        obj.work()