from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("you are riding a bike")


class Car(Vehicle):
    def start(self):
        print("You are riding a car")
