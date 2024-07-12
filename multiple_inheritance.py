class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Fish(Prey,Predator):
    pass
class Hawk(Predator):
    pass
class Rabbit(Prey):
    pass
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
fish.hunt()