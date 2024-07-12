from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod #用這個就不能創造出一個叫vehicle的類別
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You  drive the car")

    def stop(self):
        print("This car is stop")
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stop")
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.stop()