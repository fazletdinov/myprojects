class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, item):
        print("Trace:", item)
        return getattr(self.wrapped, item)

if __name__ == '__main__':
    x = Wrapper([1,2,3,4,5])
    x.append(6)
    print(x.wrapped)