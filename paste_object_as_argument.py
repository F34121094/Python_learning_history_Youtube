class Car:
    color = None
class Motorcycle:
    color = None
def change_color(car,color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike = Motorcycle()

change_color(car_1,"red")
change_color(car_3,"blue")
change_color(car_2,"white")
change_color(bike,"green")

print(car_1.color)
print(bike.color)