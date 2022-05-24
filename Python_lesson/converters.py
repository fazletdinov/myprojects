from streams import Proccesor

class Uppercase(Proccesor):
    def converter(self, data):
        return data.upper

if __name__ == ' __main__':
    import sys
    obj = Uppercase(open("spam.txt"), sys.stdout)
    obj.process()
