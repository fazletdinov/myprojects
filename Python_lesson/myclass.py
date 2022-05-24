class Ansible:
    '''Это класс ansible'''
    population = 0
    def __init__(self, name):
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        Ansible.population += 1
    def __del__(self):
        '''Уничтожение ansible'''
        print('{0} уничтожается'.format(self.name))
        Ansible.population -= 1
        if Ansible.population == 0:
            print("Все доступные ansible были уничтожены, в том числе ansible {0}".format(self.name))
        else:
            print("В настоящее время в выживщих остался всего один ansible по имени {0:d}".format(Ansible.population))
    def sayHI(self):
        print("Приветствую тебя, меня зовут {0}".format(self.name))

    def howMany():
        print("Докладываю вам, что в настоящее время нас осталось {0:d}".format(Ansible.population))
    howMany = staticmethod(howMany)
docker1 = Ansible('idel')
docker1.sayHI()
Ansible.howMany()

docker2 = Ansible('bomjur')
docker2.sayHI()
docker2.howMany()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del docker1
del docker2
Ansible.howMany()
