class Skipiter:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def next(self):
        if self.offset >= self.wrapped:
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class Skipobject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return Skipiter(self.wrapped)

if __name__ == '__main__':
    alpha = [1,2,3,4,5,6,7]
    skipper = Skipobject(alpha)

    for x in skipper:
        for y in skipper:
            print(x + y, end=" ")