class AttrDisplay:
    def _gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append("%s=%s" % (key, getattr(self, key)))
        return ",".join(attrs)
    def __str__(self):
        return "[%s: %s]" % (self.__class__.__name__, self._gatherAttrs())
if __name__ == "__main__":
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2
       # def gatherAttrs(self):
       #    return "Spam"
    class SubTest(TopTest):
        pass
    X, Y = TopTest(), SubTest()
    print(X)
    # Выведет все атрибуты экземпляра
    print(Y)
    # Выведет имя класса,
    # самого близкого в дереве наследования