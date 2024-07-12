from car import Car

car_1 = Car("Chevy", "Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_2.color)
print(car_2.make)
print(car_2.year)
print(car_2.model)

car_2.stop()
car_2.drive()