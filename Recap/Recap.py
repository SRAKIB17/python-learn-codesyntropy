class Base:
    def __init__(self):
        self.__secretKey = 2

    def x(self):
        return (self.__secretKey)

# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         self._a = 3


# obj1 = Derived()
obj2 = Base()
print(obj2.x())
