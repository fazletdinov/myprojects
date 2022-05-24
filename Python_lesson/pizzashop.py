from employees import Pizzarobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "order from", server)
    def pay(self, server):
        print(self.name, "pays for item to", server)

class Oven:
    def bake(self):
        print("oven bakes")

class Pizzashop:
    def __init__(self):
        self.server = Server("Pat")
        self.chef = Pizzarobot("Bob")
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == '__main__':
    scene = Pizzashop()
    scene.order("Homer")
    print("....")
    scene.order("Shaggy")

