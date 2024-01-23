from polymorphism import room_302


class person:
    def __init__(self):
        self.__password = 12121212
        self.name = "RAKIB"
        self.__facebook_pass = 111111

    def google_login(self):
        return self.__password


x = person()
print(x.__facebook_pass)
