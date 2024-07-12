class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def jump(self):
        print("This rabbit can jump")
class Fish(Animal):
    def swim(self):
        print("This fish can swim")
class Hawk(Animal):
    def fiy(self):
        print("This hawk cam fly")
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
rabbit.jump()
fish.swim()
print(Animal.alive)