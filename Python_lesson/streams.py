class Proccesor:
    def __init__(self, reader, write):
        self.reader = reader
        self.write = write
    def process(self):
        while 1:
            data = self.reader.redline()
            if not data: break
            data = self.converter(data)
            self.write.write(data)
    def converter(self, data):
        assert False, "CONVERTER MUST BE DEFINED"