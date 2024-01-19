class Parent:
    def __init__(self, land: int):
        self.l = land

    def display(self):
        return f'Land: {self.l}'


class Child(Parent):
    def __init__(self, land: int, buy_land: int):
        super().__init__(land)
        self.buy = buy_land
        self.l = self.l + self.buy
    #     self.id = id

    # def display(self):
    #     return self.l


x = Child(land=100, buy_land=4)
print(x.display())
