from abc import ABC, abstractmethod


class demo(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return

    def method2(self):
        print("concrete method")


obj = demo()
