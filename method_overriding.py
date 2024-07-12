class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot") #小的可以複寫大的

rabbit = Rabbit()
rabbit.eat()